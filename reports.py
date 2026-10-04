import pandas as pd
import matplotlib.pyplot as plt

from db import get_conn


def load_df():
    with get_conn() as conn:
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M").astype(str)
    return df


def monthly_summary():
    df = load_df()
    if df.empty:
        print("No data yet.")
        return None
    summary = df.groupby("month")["amount"].sum()
    print("\nMonthly totals:\n", summary.to_string())
    return summary


def category_summary():
    df = load_df()
    if df.empty:
        print("No data yet.")
        return None
    summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    print("\nCategory totals:\n", summary.to_string())
    return summary


def pie_chart():
    summary = category_summary()
    if summary is None:
        return
    summary.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
    plt.title("Spending by Category")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


def bar_chart():
    summary = monthly_summary()
    if summary is None:
        return
    summary.plot(kind="bar", figsize=(8, 5), color="steelblue")
    plt.title("Spending by Month")
    plt.xlabel("Month")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
