# キュースキーマ / ジョブ契約

## ジョブ種別
- `stream.segment`: ストリーム中間/確定セグメント
- `batch.transcribe`: バッチ推論

## `batch.transcribe` payload
```json
{
  "jobId": "uuid",
  "projectId": "proj_...",
  "sourceUri": "s3://bucket/key.wav",
  "language": "ja-JP",
  "options": { "punctuation": true, "diarization": true },
  "callback": { "event": "transcription.completed", "url": "https://...", "secret": "..." }
}
```

## 再試行ポリシー
- 退避: 2^n 秒、最大 6 回、上限 5 分
- 冪等性キー: `jobId`

## 可観測性
- 属性: traceId, spanId, enqueueTs, startTs, endTs, attempts