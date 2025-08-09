# シーケンス（テキスト表現）

## ストリーミング STT
Client → API(WS): init
Client → API(WS): audio(chunk)*
API → Ingestion: chunk enqueue
Ingestion → Worker: chunks → partial/final
Worker → Ingestion: results
API(WS) → Client: partial/final

## バッチ STT
Client → API(REST): upload
API → Storage: save
API → Queue: enqueue(job)
Worker → Storage/DB: read/write
Client → API: status/result