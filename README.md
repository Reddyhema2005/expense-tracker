# Expense Tracker

A command-line app to log daily expenses, store them in SQLite, and view monthly and category-wise reports with charts.

## Features

- Add, view, edit, and delete expenses
- Data stored locally in SQLite (`sqlite3`)
- Monthly and category totals using `pandas`
- Pie chart (by category) and bar chart (by month) using `matplotlib`
- Input validation for amounts and dates

## Tech Stack

Python, SQLite, pandas, matplotlib

## Project Structure

```
expense-tracker/
├── main.py           # CLI menu
├── db.py             # SQLite database functions
├── reports.py        # pandas summaries and charts
├── requirements.txt
└── README.md
```

## Getting Started

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
pip install -r requirements.txt
python main.py
```

## Usage

Run `main.py` and choose an option from the menu:

```
1. Add expense          5. Monthly summary
2. View expenses        6. Category summary
3. Edit expense         7. Pie chart (by category)
4. Delete expense       8. Bar chart (by month)
0. Exit
```

## Future Improvements

- Streamlit dashboard
- Export reports to CSV/Excel
- Monthly budget alerts

## Author

Reddyhema Vuyyala
