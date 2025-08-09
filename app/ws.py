from __future__ import annotations
import json
from typing import Any, Dict, Optional
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import WebSocketRoute


class StreamEndpoint(WebSocketEndpoint):
    encoding = "text"

    async def on_connect(self, websocket):
        await websocket.accept()
        self.seq_seen = -1

    async def on_receive(self, websocket, data):
        try:
            if isinstance(data, bytes):
                self.seq_seen += 1
                await websocket.send_text(json.dumps({"type": "partial", "seq": self.seq_seen, "text": "binary chunk ok", "confidence": 0.7}))
                return
            obj = json.loads(data)
        except Exception:
            await websocket.send_text(json.dumps({"type": "error", "code": "VALIDATION_ERROR", "message": "invalid json"}))
            return
        mtype = obj.get("type")
        if mtype == "init":
            await websocket.send_text(json.dumps({"type": "partial", "seq": 0, "text": "init ok", "confidence": 1.0}))
        elif mtype == "audio":
            seq = int(obj.get("seq", -1))
            self.seq_seen = max(self.seq_seen, seq)
            await websocket.send_text(json.dumps({"type": "partial", "seq": seq, "text": f"processing seq {seq}", "confidence": 0.8}))
        elif mtype == "close":
            final_payload: Dict[str, Any] = {
                "type": "final",
                "segment": {
                    "startMs": 0,
                    "endMs": 1000,
                    "text": "最終確定（ダミー）",
                    "speakerId": "spk_1",
                    "confidence": 0.9,
                },
            }
            await websocket.send_text(json.dumps(final_payload, ensure_ascii=False))
            await websocket.close()
        else:
            await websocket.send_text(json.dumps({"type": "error", "code": "VALIDATION_ERROR", "message": "unknown type"}))


ws_routes = [
    WebSocketRoute("/v1/stream", StreamEndpoint),
]