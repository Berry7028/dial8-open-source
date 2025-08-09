# データ要件

## エンティティ
- Transcript: id, projectId, source, language, duration, createdAt, status
- Segment: id, transcriptId, startMs, endMs, text, speakerId, confidence
- Speaker: id, label, embedding(optional)

## 保持/削除
- 既定保持 90 日（設定可能）、プロジェクト毎のポリシー
- 即時削除 API、バックアップからの除外 SLA

## 品質/整合性
- タイムスタンプ精度 ±50ms、文字コード UTF-8
- PII マスキング（オプション）