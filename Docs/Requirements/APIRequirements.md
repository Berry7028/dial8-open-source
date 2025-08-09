# API 要件

## REST（バッチ）
- POST /v1/transcriptions: 音声アップロード（multipart、URL 参照も可）
- GET /v1/transcriptions/{id}: 状態照会
- GET /v1/transcriptions/{id}/result: 結果（json/txt/vtt）

## WebSocket（ストリーミング）
- wss://.../v1/stream?lang=ja-JP&project=...&token=...
- メッセージ種別: init, audio, partial, final, error, close

## Webhook/Events
- transcription.completed, transcription.failed

## 共通
- 認証: API キー（ヘッダ）/OAuth2（後続）
- レート制限、冪等性キー、エラーコード規約