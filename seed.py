import sqlite3
import app
import time

DBNAME = "termtrader.db"

def seed(dbname):
    with sqlite3.connect(dbname) as conn:
        SQL = "DELETE FROM {};"
        cur = conn.cursor()
        cur.execute(SQL.format('accounts'))
        cur.execute(SQL.format('positions'))
        cur.execute(SQL.format('trades'))

    account = app.Account()
    account.username = "carter"
    account.balance = 1000.0
    account.set_password(app.util.hash_pass("password"))
    account.api_key='000000000000000'
    account.save()

    position = app.Position()
    position.account_pk = 1
    position.ticker = 'tsla'
    position.shares = 5
    position.save()

    trade1 = app.Trade()
    trade1.time = time.time() - 24 * 60 * 60
    trade1.ticker = 'tsla'
    trade1.account_pk = 1
    trade1.volume = 10
    trade1.price = app.util.get_price('tsla') - 20.0
    trade1.save()

    trade2 = app.Trade()
    trade2.time = time.time()
    trade2.ticker = 'tsla'
    trade2.account_pk = 1
    trade2.volume = -5
    trade2.price = app.util.get_price('tsla') + 20.0
    trade2.save()



if __name__ == "__main__":
    seed(DBNAME)
