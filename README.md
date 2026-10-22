# Expense Tracker

A Python terminal application I am building while learning software development.

## Current Features

- Record expenses with today's date, category, amount, and expense type.
- Normalize category names to uppercase.
- Choose between regular and monthly expenses.
- Accept only positive whole-number amounts.
- Handle invalid amount input without crashing.
- Calculate spending totals by category.

## How to Run

Open a terminal in the project folder.

Create a virtual environment if you haven't already:

```bash
python3 -m venv .venv
```

Activate it on macOS:

```bash
source .venv/bin/activate
```

Run the application:

```bash
python main.py
```

Enter a category and amount, then select:
- `1` for regular expenses
- `2` for monthly expenses

Enter `done` at the category prompt to finish and view totals.

## Current Limitations

- Expenses are stored in memory and are lost when the program closes.
- Amounts support whole rupees only.
- Category totals currently combine all recorded dates and expense types.

## Next Steps

- Separate regular and monthly spending in reports.
- Filter expenses by date to calculate weekly category totals.
- Save and load expenses from a file.
- Calculate remaining pocket money and estimate savings.