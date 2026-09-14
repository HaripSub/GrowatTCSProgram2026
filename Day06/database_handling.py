"""
db_handler.py — Minimal SQLite helper with simple CLI for insert/list/update/delete

Features:
- SimpleDB class with basic CRUD helpers
- insert_many, update (by SQL), delete_by_id, delete_one_user_by_name
- CLI menu that asks the user for input to update or delete rows
- Uses only Python stdlib (sqlite3, os, re)
"""

import os
import re
import sqlite3
from typing import Any, Dict, Iterable, List, Optional

_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


class SimpleDB:
    def __init__(self, path: str = "app.db"):
        if path != ":memory:":
            path = os.path.abspath(os.path.expanduser(path))
            parent = os.path.dirname(path)
            if parent and not os.path.exists(parent):
                os.makedirs(parent, exist_ok=True)
        self.path = path
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def close(self) -> None:
        self.conn.close()

    def _validate_identifier(self, name: str) -> None:
        if not _IDENTIFIER_RE.match(name):
            raise ValueError(f"Invalid identifier: {name!r}")

    def execute(self, sql: str, params: Iterable[Any] = ()) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def insert(self, sql: str, params: Iterable[Any] = ()) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        self.conn.commit()
        last = cur.lastrowid
        cur.close()
        return last

    def insert_many(self, sql: str, params_seq: Iterable[Iterable[Any]]) -> int:
        cur = self.conn.cursor()
        cur.executemany(sql, [tuple(p) for p in params_seq])
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def update(self, sql: str, params: Iterable[Any] = ()) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete(self, sql: str, params: Iterable[Any] = ()) -> int:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_by_id(self, table: str, id_value: Any) -> int:
        self._validate_identifier(table)
        sql = f"DELETE FROM {table} WHERE id = ?"
        cur = self.conn.cursor()
        cur.execute(sql, (id_value,))
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def delete_one_user_by_name(self, name: str) -> int:
        cur = self.conn.cursor()
        cur.execute(
            "DELETE FROM users WHERE rowid = (SELECT rowid FROM users WHERE name = ? LIMIT 1)",
            (name,),
        )
        self.conn.commit()
        rc = cur.rowcount
        cur.close()
        return rc

    def fetchone(self, sql: str, params: Iterable[Any] = ()) -> Optional[Dict[str, Any]]:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        row = cur.fetchone()
        cur.close()
        return dict(row) if row else None

    def fetchall(self, sql: str, params: Iterable[Any] = ()) -> List[Dict[str, Any]]:
        cur = self.conn.cursor()
        cur.execute(sql, tuple(params))
        rows = cur.fetchall()
        cur.close()
        return [dict(r) for r in rows]


def prompt_users_from_input() -> List[tuple]:
    """
    Ask the user to enter multiple users in the form:
      name:email,name:email,...
    or enter a single "name:email".
    Returns list of tuples [(name,email), ...]
    """
    s = input("Enter users as name:email separated by commas (e.g. Alice:alice@x.com,Bob:bob@x.com): ").strip()
    if not s:
        return []
    pairs = [p.strip() for p in s.split(",") if p.strip()]
    out = []
    for p in pairs:
        if ":" not in p:
            print(f"Skipping invalid entry (no colon): {p!r}")
            continue
        name, email = p.split(":", 1)
        out.append((name.strip(), email.strip()))
    return out


def main():
    db = SimpleDB("app.db")
    print("Database path:", db.path)

    # Ensure table exists
    db.execute(
        """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """
    )

    while True:
        print("\nMenu:")
        print("  1) List users")
        print("  2) Insert users")
        print("  3) Update user by id")
        print("  4) Delete user by id")
        print("  5) Delete one user by name")
        print("  6) Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            users = db.fetchall("SELECT id, name, email FROM users ORDER BY id")
            if users:
                for u in users:
                    print(f"{u['id']:>3}: {u['name']} <{u['email']}>")
            else:
                print("No users found.")

        elif choice == "2":
            users = prompt_users_from_input()
            if not users:
                print("No users provided.")
                continue
            # Use INSERT OR IGNORE to skip duplicates
            count = db.insert_many("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", users)
            print("insert_many returned (rowcount):", count)
            # show inserted/existing
            for _, email in users:
                row = db.fetchone("SELECT id, name, email FROM users WHERE email = ?", (email,))
                print(" ->", row)

        elif choice == "3":
            id_str = input("Enter user id to update: ").strip()
            if not id_str.isdigit():
                print("Invalid id.")
                continue
            user_id = int(id_str)
            # Fetch current
            cur = db.fetchone("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
            if not cur:
                print("User not found.")
                continue
            print("Current:", cur)
            new_name = input("Enter new name (leave empty to keep): ").strip()
            new_email = input("Enter new email (leave empty to keep): ").strip()
            if not new_name and not new_email:
                print("Nothing to update.")
                continue
            # Build update statement
            parts = []
            params = []
            if new_name:
                parts.append("name = ?")
                params.append(new_name)
            if new_email:
                parts.append("email = ?")
                params.append(new_email)
            params.append(user_id)
            sql = f"UPDATE users SET {', '.join(parts)} WHERE id = ?"
            try:
                rows = db.update(sql, params)
                print("Rows updated:", rows)
                print("Now:", db.fetchone("SELECT id, name, email FROM users WHERE id = ?", (user_id,)))
            except sqlite3.IntegrityError as e:
                print("Error updating (likely duplicate email):", e)

        elif choice == "4":
            id_str = input("Enter user id to delete: ").strip()
            if not id_str.isdigit():
                print("Invalid id.")
                continue
            user_id = int(id_str)
            rows = db.delete_by_id("users", user_id)
            print("Rows deleted:", rows)

        elif choice == "5":
            name = input("Enter name to delete one matching row: ").strip()
            if not name:
                print("Empty name.")
                continue
            rows = db.delete_one_user_by_name(name)
            print("Rows deleted (0 or 1):", rows)

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid choice, enter 1-6.")

    db.close()


if __name__ == "__main__":
    main()