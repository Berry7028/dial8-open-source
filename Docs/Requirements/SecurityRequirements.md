# セキュリティ要件

- 通信: TLS1.2+、HSTS、Secure Cookie 不使用（API）
- 保存: 暗号化（KMS）、鍵のローテーション
- 認証: API キー（スコープ付与）、将来 SSO/OAuth2
- 認可: プロジェクト単位 RBAC（Admin/Editor/Reader）
- ログ: アクセス監査、PII レッドアクション
- 脆弱性: 依存関係スキャン、イメージ署名、CVE SLA