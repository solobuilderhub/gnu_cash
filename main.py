from piecash import open_book, Account, Transaction, Split
from datetime import datetime, date
from decimal import Decimal

# PostgreSQL connection string with schema in the search path
connection_string = "postgresql://postgres:7atInThNbl18lhRvbh7G0qreItnfcVTP3wFWuGyc7E5OoUIGfl5dxgou1TlRxwf0@188.245.189.26:5432/gnucash"

# Open the GnuCash book
with open_book(uri_conn=connection_string, readonly=False, do_backup=False) as book:
    print("Book opened successfully")
    print(book.default_currency)

    # Print all accounts
    print("Accounts in the book:")
    for account in book.accounts:
        # if account.type == "INCOME":
        #     print(f"Splites in account {account.splits}")
        #     break
        print(f"Account name: {account.name}, Full name: {account.fullname}, Type: {account.type}, Commodity: {account.commodity.mnemonic}, Description: {account.description}")

    # Get a specific account by full name
    # account_fullname = "Expenses:Auto:Fuel"  # Replace with the actual account full name
    # specific_account = next((acc for acc in book.accounts if acc.fullname == account_fullname), None)
    
    # if specific_account:
    #     print(f"\nFound account by full name: {specific_account.fullname}")
    #     print(f"Account name: {specific_account.name}, Type: {specific_account.type}, Commodity: {specific_account.commodity.mnemonic}, Description: {specific_account.description}")
    # else:
    #     print(f"\nAccount with full name '{account_fullname}' not found.")