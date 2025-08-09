# SuperWhisper ドキュメント

本リポジトリは「SuperWhisper（リアルタイム高精度 音声→テキスト基盤）」のプロジェクトドキュメントです。構想、要件、設計、運用、開発判断（ADR）までを網羅します。

- 目的: 高精度・低遅延・多言語のストリーミング音声認識と、検索・編集・連携可能なトランスクリプト基盤を提供
- 想定利用: 会議、コールセンター、字幕生成、ボイスボット、音声メモ、議事録、バリアフリー支援 等

## 構成
- `ROADMAP.md`: 全体ロードマップ
- `Requirements/`: PRD/要件定義（機能/非機能/API/セキュリティ/データ/受け入れ）
- `Architecture/`: システム構成、設計、データモデル、シーケンス、スケーリング
- `Development/ADRs/`: 重要な技術判断の記録
- `UX/`: ペルソナ、ユーザージャーニー、UX原則
- `Operations/`: 監視、運用手順、インシデント対応、容量計画
- `ProjectManagement/`: マイルストーン、リリース、RACI、リスク
- `Deployment/`: CI/CD、環境、インフラ
- `Monetization/`: 料金、メトリクス
- `Localization/`: i18n/l10n 計画
- `Compliance/`: プライバシー/アクセシビリティ/ライセンス
- `Appendix/Glossary.md`: 用語集

## ガイドライン
- ドキュメントは日本語で作成（API/プロトコル名は英語可）
- 変更は PR ベースでレビューし、該当 ADR を更新
- 重大な要件変更は `Requirements/` と `ROADMAP.md` を同期