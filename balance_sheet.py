from piecash import open_book
from decimal import Decimal

# PostgreSQL connection string with schema in the search path
connection_string = "postgresql://postgres:7atInThNbl18lhRvbh7G0qreItnfcVTP3wFWuGyc7E5OoUIGfl5dxgou1TlRxwf0@188.245.189.26:5432/gnucash"

# Open the GnuCash book
with open_book(uri_conn=connection_string, readonly=False, do_backup=False) as book:
    print("Book opened successfully")
    print(f"Default currency: {book.default_currency}")

    # Initialize balance sheet categories
    assets = Decimal('0.0')
    liabilities = Decimal('0.0')
    equity = Decimal('0.0')

    # Iterate over accounts and categorize them
    for account in book.accounts:
        if account.type == "ASSET" and ":" not in account.fullname:
            balance = account.get_balance()
            print(f"Account: {account.fullname}, Balance: {balance}")
            assets += account.get_balance()
        elif account.type == "LIABILITY" and ":" not in account.fullname:
            balance = account.get_balance()
            print(f"Account: {account.fullname}, Balance: {balance}")
            liabilities += account.get_balance()
        elif account.type == "EQUITY" and ":" not in account.fullname:
            balance = account.get_balance()
            print(f"Account: {account.fullname}, Balance: {balance}")
            equity += account.get_balance()

    # Print the balance sheet
    print("\n\n\nBalance Sheet:")
    print(f"Assets: {assets}")
    print(f"Liabilities: {liabilities}")
    print(f"Equity: {equity}")
    print(f"Total: {assets - liabilities + equity}")