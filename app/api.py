from __future__ import annotations
import uuid
from typing import Optional
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse, PlainTextResponse, Response
from starlette.background import BackgroundTask
from starlette.datastructures import FormData
from .storage import get_conn, create_transcript, get_transcript, get_result
from .worker import simulate_transcription_job


async def create_transcription(request: Request) -> Response:
    form: FormData = await request.form()
    language: str = str(form.get("language") or "ja-JP")
    source_url: Optional[str] = form.get("sourceUrl")  # type: ignore
    file = form.get("file")
    if not source_url and not file:
        return JSONResponse({"error": {"code": "VALIDATION_ERROR", "message": "file or sourceUrl required"}}, status_code=422)
    tr_id = f"tr_{uuid.uuid4().hex[:12]}"
    conn = get_conn()
    create_transcript(conn, tr_id, language)
    task = BackgroundTask(simulate_transcription_job, tr_id, language, source_url)
    return JSONResponse({"id": tr_id, "status": "queued"}, status_code=202, background=task)


async def get_status(request: Request) -> Response:
    tr_id = request.path_params["tr_id"]
    conn = get_conn()
    row = get_transcript(conn, tr_id)
    if not row:
        return JSONResponse({"error": {"code": "NOT_FOUND", "message": "Transcript not found"}}, status_code=404)
    return JSONResponse({"id": row["id"], "status": row["status"], "progress": row["progress"]})


async def get_result_endpoint(request: Request) -> Response:
    tr_id = request.path_params["tr_id"]
    format_q = request.query_params.get("format", "json")
    conn = get_conn()
    data = get_result(conn, tr_id)
    if data is None:
        row = get_transcript(conn, tr_id)
        if not row:
            return JSONResponse({"error": {"code": "NOT_FOUND", "message": "Transcript not found"}}, status_code=404)
        return JSONResponse({"error": {"code": "CONFLICT", "message": "Result not ready"}}, status_code=409)
    if format_q == "json":
        return JSONResponse(data)
    elif format_q == "txt":
        text = "\n".join(seg.get("text", "") for seg in data.get("segments", []))
        return PlainTextResponse(text)
    elif format_q == "vtt":
        lines = ["WEBVTT"]
        for idx, seg in enumerate(data.get("segments", []), start=1):
            start_ms, end_ms = seg.get("startMs", 0), seg.get("endMs", 0)
            def fmt(ms: int) -> str:
                s, ms = divmod(ms, 1000)
                m, s = divmod(s, 60)
                h, m = divmod(m, 60)
                return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"
            lines.append(str(idx))
            lines.append(f"{fmt(start_ms)} --> {fmt(end_ms)}")
            lines.append(seg.get("text", ""))
            lines.append("")
        return PlainTextResponse("\n".join(lines))
    else:
        return JSONResponse({"error": {"code": "BAD_REQUEST", "message": "Unsupported format"}}, status_code=400)


routes = [
    Route("/v1/transcriptions", create_transcription, methods=["POST"]),
    Route("/v1/transcriptions/{tr_id}", get_status, methods=["GET"]),
    Route("/v1/transcriptions/{tr_id}/result", get_result_endpoint, methods=["GET"]),
]