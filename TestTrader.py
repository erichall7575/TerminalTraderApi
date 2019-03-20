from app import Account
account = Account.from_pk(1)
sometrades = account.get_trades()
print(sometrades)