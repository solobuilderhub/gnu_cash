from piecash import open_book, Account, Commodity

# PostgreSQL connection string with schema in the search path
connection_string = "postgresql://postgres:7atInThNbl18lhRvbh7G0qreItnfcVTP3wFWuGyc7E5OoUIGfl5dxgou1TlRxwf0@188.245.189.26:5432/gnucash"

# Open the GnuCash book
with open_book(uri_conn=connection_string, readonly=False, do_backup=False) as book:
    print("Book opened successfully")
    print(book.default_currency)

    # Find the parent account (Assets)
    parent_account = next((acc for acc in book.accounts if acc.fullname == "Assets"), None)
    
    if parent_account:
        # Retrieve the existing USD currency
        usd_currency = next((comm for comm in book.commodities if comm.mnemonic == "USD"), None)
        
        if usd_currency:
            # Create the new account under Assets
            new_account = Account(
                name="Equipment",
                type="ASSET",
                parent=parent_account,
                commodity=usd_currency,
                description="Equipment Asset account"
            )
            
            # Save the changes to the book
            book.save()
            print(f"Created new account: {new_account.fullname}")
        else:
            print("USD currency not found.")
    else:
        print("Parent account 'Assets' not found.")