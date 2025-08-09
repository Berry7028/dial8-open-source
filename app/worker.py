from __future__ import annotations
import time
import uuid
from typing import Optional, Dict, Any
from .storage import get_conn, update_status, save_result


def simulate_transcription_job(tr_id: str, language: str, source: Optional[str]) -> None:
    conn = get_conn()
    # Simulate progress
    for i in range(1, 6):
        time.sleep(0.2)  # fast for tests
        update_status(conn, tr_id, "processing", progress=i * 0.15)
    # Produce a fake result
    segment = {
        "startMs": 0,
        "endMs": 1200,
        "text": "これはダミーの書き起こし結果です",
        "speakerId": "spk_1",
        "confidence": 0.95,
    }
    result: Dict[str, Any] = {"id": tr_id, "language": language, "segments": [segment]}
    save_result(conn, tr_id, result)