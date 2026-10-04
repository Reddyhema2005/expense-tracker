
from datetime import datetime

import db
import reports


def ask_amount(prompt="Amount: "):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Enter a positive number.")


def ask_date(prompt="Date (YYYY-MM-DD, blank = today): "):
    while True:
        raw = input(prompt).strip()
        if not raw:
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("Use the format YYYY-MM-DD.")


def ask_id(prompt="Expense ID: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid ID.")


def add():
    amount = ask_amount()
    category = input("Category: ").strip().title() or "Other"
    date = ask_date()
    note = input("Note (optional): ").strip()
    db.add_expense(amount, category, date, note)
    print("Expense added.")


def view():
    rows = db.get_expenses()
    if not rows:
        print("No expenses yet.")
        return
    print(f"\n{'ID':<4} {'Date':<12} {'Category':<14} {'Amount':>10}  Note")
    print("-" * 55)
    for id_, amount, category, date, note in rows:
        print(f"{id_:<4} {date:<12} {category:<14} {amount:>10.2f}  {note or ''}")


def edit():
    view()
    expense_id = ask_id()
    amount = ask_amount("New amount: ")
    category = input("New category: ").strip().title() or "Other"
    date = ask_date("New date (YYYY-MM-DD, blank = today): ")
    note = input("New note: ").strip()
    ok = db.update_expense(expense_id, amount, category, date, note)
    print("Updated." if ok else "ID not found.")


def delete():
    view()
    ok = db.delete_expense(ask_id())
    print("Deleted." if ok else "ID not found.")


MENU = """
===== Expense Tracker =====
1. Add expense
2. View expenses
3. Edit expense
4. Delete expense
5. Monthly summary
6. Category summary
7. Pie chart (by category)
8. Bar chart (by month)
0. Exit
"""

ACTIONS = {
    "1": add,
    "2": view,
    "3": edit,
    "4": delete,
    "5": reports.monthly_summary,
    "6": reports.category_summary,
    "7": reports.pie_chart,
    "8": reports.bar_chart,
}


def main():
    db.init_db()
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
