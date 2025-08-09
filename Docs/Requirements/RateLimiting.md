# レート制限

- バッチ REST: 60 req/min/プロジェクト、バースト 120
- ストリーミング WS: 同時接続 20/プロジェクト、バースト 50、アイドル切断 60s
- エラーレスポンス: 429 + `Retry-After`、`error.code=RATE_LIMIT`