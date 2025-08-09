# API 契約（REST）

## POST /v1/transcriptions
- 認証: `Authorization: Bearer <API_KEY>`
- 入力: multipart/form-data（`file` または `sourceUrl`）
- 出力: 202 + location ヘッダ
```json
{ "id": "tr_123", "status": "queued" }
```

## GET /v1/transcriptions/{id}
```json
{ "id": "tr_123", "status": "processing", "progress": 0.36 }
```

## GET /v1/transcriptions/{id}/result?format=json
```json
{
  "id": "tr_123",
  "language": "ja-JP",
  "segments": [
    { "startMs": 0, "endMs": 1200, "text": "おはようございます", "speakerId": "spk_1", "confidence": 0.94 }
  ]
}
```

## エラー
```json
{ "error": { "code": "NOT_FOUND", "message": "Transcript not found" } }
```