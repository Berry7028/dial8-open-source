from __future__ import annotations
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json().get("ok") is True


def test_create_and_get_transcription_result_flow():
    r = client.post("/v1/transcriptions", data={"language": "ja-JP", "sourceUrl": "https://example.com/a.wav"})
    assert r.status_code == 202
    tr_id = r.json()["id"]

    r2 = client.get(f"/v1/transcriptions/{tr_id}")
    assert r2.status_code == 200

    import time
    time.sleep(1.0)

    r3 = client.get(f"/v1/transcriptions/{tr_id}/result?format=json")
    assert r3.status_code == 200
    body = r3.json()
    assert body["id"] == tr_id
    assert isinstance(body.get("segments"), list)