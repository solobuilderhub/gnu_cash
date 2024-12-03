from piecash import open_book
from decimal import Decimal
from datetime import date

# PostgreSQL connection string with schema in the search path
connection_string = "postgresql://postgres:7atInThNbl18lhRvbh7G0qreItnfcVTP3wFWuGyc7E5OoUIGfl5dxgou1TlRxwf0@188.245.189.26:5432/gnucash"

# Open the GnuCash book
with open_book(uri_conn=connection_string, readonly=False, do_backup=False) as book:
    print("Book opened successfully")
    print(f"Default currency: {book.default_currency}")

    # Initialize cash flow categories
    operating_activities = Decimal('0.0')
    investing_activities = Decimal('0.0')
    financing_activities = Decimal('0.0')

    # Define the period for the cash flow report
    start_date = date(2024, 1, 1)
    end_date = date(2024, 12, 31)

    # Iterate over transactions and categorize them
    for transaction in book.transactions:
        if start_date <= transaction.post_date <= end_date:
            for split in transaction.splits:
                if split.account.type == "INCOME" or split.account.type == "EXPENSE":
                    operating_activities += split.value
                elif split.account.type == "ASSET":
                    investing_activities += split.value
                elif split.account.type == "LIABILITY" or split.account.type == "EQUITY":
                    financing_activities += split.value

    # Print the cash flow report
    print("\nCash Flow Report:")
    print(f"Operating Activities: {operating_activities}")
    print(f"Investing Activities: {investing_activities}")
    print(f"Financing Activities: {financing_activities}")
    print(f"Net Cash Flow: {operating_activities + investing_activities + financing_activities}")