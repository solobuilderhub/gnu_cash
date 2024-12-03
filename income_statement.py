from piecash import open_book
from decimal import Decimal
from datetime import date

# PostgreSQL connection string with schema in the search path
connection_string = "postgresql://postgres:7atInThNbl18lhRvbh7G0qreItnfcVTP3wFWuGyc7E5OoUIGfl5dxgou1TlRxwf0@188.245.189.26:5432/gnucash"

# Open the GnuCash book
with open_book(uri_conn=connection_string, readonly=False, do_backup=False) as book:
    print("Book opened successfully")
    print(f"Default currency: {book.default_currency}")

    # Initialize income statement categories
    revenues = Decimal('0.0')
    expenses = Decimal('0.0')

    # Define the period for the income statement
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)

    # Iterate over accounts and categorize them
    for account in book.accounts:
        if account.type == "INCOME":
            for split in account.splits:
                if start_date <= split.transaction.post_date <= end_date:
                    revenues += split.value
        elif account.type == "EXPENSE":
            for split in account.splits:
                if start_date <= split.transaction.post_date <= end_date:
                    expenses += split.value

    # Calculate net income
    net_income = revenues - expenses

    # Print the income statement
    print("\nIncome Statement:")
    print(f"Revenues: {revenues}")
    print(f"Expenses: {expenses}")
    print(f"Net Income: {net_income}")