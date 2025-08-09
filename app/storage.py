from __future__ import annotations
import json
import os
import sqlite3
from datetime import datetime
from typing import Optional

DB_PATH = os.environ.get("APP_DB_PATH", "/workspace/data/app.db")


def _ensure_dir(path: str) -> None:
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def get_conn() -> sqlite3.Connection:
    _ensure_dir(DB_PATH)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    _init_schema(conn)
    return conn


def _init_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS transcripts (
          id TEXT PRIMARY KEY,
          language TEXT,
          status TEXT,
          created_at TEXT,
          progress REAL,
          result_json TEXT
        );
        """
    )
    conn.commit()


def create_transcript(conn: sqlite3.Connection, tr_id: str, language: str) -> None:
    conn.execute(
        "INSERT INTO transcripts (id, language, status, created_at, progress, result_json) VALUES (?, ?, ?, ?, ?, ?)",
        (tr_id, language, "queued", datetime.utcnow().isoformat(), 0.0, None),
    )
    conn.commit()


def update_status(conn: sqlite3.Connection, tr_id: str, status: str, progress: Optional[float] = None) -> None:
    conn.execute(
        "UPDATE transcripts SET status = ?, progress = COALESCE(?, progress) WHERE id = ?",
        (status, progress, tr_id),
    )
    conn.commit()


def save_result(conn: sqlite3.Connection, tr_id: str, result: dict) -> None:
    conn.execute(
        "UPDATE transcripts SET status = ?, progress = ?, result_json = ? WHERE id = ?",
        ("completed", 1.0, json.dumps(result, ensure_ascii=False), tr_id),
    )
    conn.commit()


def get_transcript(conn: sqlite3.Connection, tr_id: str) -> Optional[sqlite3.Row]:
    cur = conn.execute("SELECT * FROM transcripts WHERE id = ?", (tr_id,))
    row = cur.fetchone()
    return row


def get_result(conn: sqlite3.Connection, tr_id: str) -> Optional[dict]:
    row = get_transcript(conn, tr_id)
    if not row:
        return None
    if row["result_json"] is None:
        return None
    return json.loads(row["result_json"])  # type: ignore