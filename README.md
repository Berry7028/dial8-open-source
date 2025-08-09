# SuperWhisper (skeleton)

This is a minimal runnable skeleton implementing the Docs MVP: REST batch transcription endpoints and a WebSocket streaming endpoint (stubbed processing).

## Run (dev)

- Install deps:
  ```bash
  pip install -r requirements.txt
  ```
- Start server:
  ```bash
  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```

## Endpoints
- REST: POST /v1/transcriptions, GET /v1/transcriptions/{id}, GET /v1/transcriptions/{id}/result
- WS:   ws://localhost:8000/v1/stream

## Tests
```bash
pytest -q
```