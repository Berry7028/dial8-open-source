# データモデル（概略）

```
Project (id, name, plan, settings)
  └── Transcript (id, projectId, language, source, duration, status, createdAt)
        └── Segment (id, transcriptId, startMs, endMs, text, speakerId, confidence)
Speaker (id, label)
WebhookSubscription (id, projectId, event, url, secret)
ApiKey (id, projectId, scopes, createdAt, lastUsedAt)
```

- インデックス: (transcriptId, startMs), (projectId, createdAt)
- 保持: Transcript/Segment は同一リージョンで保管
