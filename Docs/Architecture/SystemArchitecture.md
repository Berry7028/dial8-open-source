# システムアーキテクチャ（高レベル）

## コンポーネント
- API Gateway: REST/WebSocket、認証・レート制限
- Ingestion Service: 音声受信/前処理、ストリーミング分割
- Transcription Workers: GPU 上で音声→テキスト（Whisper/派生モデル）
- Job Queue: バッチ/ストリーム処理、優先度制御
- Storage: オブジェクト（音声）、DB（メタ/セグメント）、VectorDB（検索）
- Webhook/Events: 外部通知
- Admin/Console: 運用・可観測性・設定

## データフロー
1) クライアント→API→Ingestion
2) キュー→Worker（GPU）
3) 結果→DB/オブジェクト→API 経由で返却/通知

## 可観測性
- Metrics/Tracing/Logs、SLO ダッシュボード、エラーバジェット