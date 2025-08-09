# コンポーネント設計

## API Gateway
- 認証（API キー）、WS 升格、レート制限

## Ingestion Service
- 音声チャンク化、フォーマット変換（Opus/PCM 16kHz mono）
- 冪等性キー、リトライ

## Transcription Worker
- モデル推論（Whisper/蒸留版/量子化版）、バッチ/ストリーム両対応
- 辞書補正、句読点/整形、話者分離

## Persistence
- Postgres（トランスクリプト/セグメント）、S3 互換（音声）
- Vector 検索（セマンティック）

## Admin/Console
- メトリクス、アラート、ジョブ管理、監査ビュー