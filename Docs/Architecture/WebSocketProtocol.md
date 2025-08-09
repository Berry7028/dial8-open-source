# WebSocket プロトコル仕様（ストリーミング STT）

## 接続
- URL: `wss://{host}/v1/stream`
- Query: `lang`, `project`, `token`, `format=pcm16|opus`
- サブプロトコル: なし

## メッセージ形式
すべて JSON（バイナリ音声は別チャンク）

### init（client → server）
```json
{
  "type": "init",
  "sessionId": "uuid",
  "language": "ja-JP",
  "sampleRate": 16000,
  "audioFormat": "pcm16",
  "enablePunctuation": true,
  "enableDiarization": false,
  "customVocabulary": ["固有名詞A", "製品名B"]
}
```

### audio（client → server, binary or base64）
- 1 チャンクあたり 20–60ms 推奨
- ヘッダ（JSON）→ 直後にバイナリ
```json
{ "type": "audio", "seq": 12, "timestampMs": 123456 }
```

### partial（server → client）
```json
{ "type": "partial", "seq": 12, "text": "途中の文字列", "confidence": 0.78 }
```

### final（server → client）
```json
{
  "type": "final",
  "segment": {
    "startMs": 12340,
    "endMs": 17890,
    "text": "確定した文字列",
    "speakerId": "spk_1",
    "confidence": 0.92
  }
}
```

### error（server → client）
```json
{ "type": "error", "code": "RATE_LIMIT", "message": "Too many streams" }
```

### close（双方）
```json
{ "type": "close", "reason": "client_done" }
```

## 冪等性/順序
- `seq` により乱序を許容しつつ再構成
- 欠落検出で `nack` を返すことがある

## タイムアウト/再接続
- `ping/pong` 30s、無通信 60s で切断
- 再接続時は `sessionId` 指定で継続（最大 2 分）