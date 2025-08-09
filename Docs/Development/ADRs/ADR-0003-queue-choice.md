# ADR-0003: キュー選定（例: Kafka or Redis Streams）

- ステータス: Proposed
- 候補: Kafka（スループット/リテンション）、Redis Streams（簡易/低レイテンシ）
- 決定基準: 運用負荷、可観測性、順序保証、コスト