import sqlite3

DB_NAME = "expenses.db"


def get_conn():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                note TEXT
            )
        """)


def add_expense(amount, category, date, note=""):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
            (amount, category, date, note),
        )


def get_expenses():
    with get_conn() as conn:
        return conn.execute(
            "SELECT id, amount, category, date, note FROM expenses ORDER BY date DESC"
        ).fetchall()


def update_expense(expense_id, amount, category, date, note=""):
    with get_conn() as conn:
        cur = conn.execute(
            "UPDATE expenses SET amount=?, category=?, date=?, note=? WHERE id=?",
            (amount, category, date, note, expense_id),
        )
        return cur.rowcount > 0


def delete_expense(expense_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        return cur.rowcount > 0
