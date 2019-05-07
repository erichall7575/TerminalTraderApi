import time
import random
import string
from app.orm import ORM
from app.util import hash_pass
from app.util import get_price
from app.util import get_allprice
from app.util import get_allpricesearch
from app.position import Position
from app.trade import Trade


SALT = "nobody will ever guess this"


class Account(ORM):
    fields = ["username", "password_hash","api_key", "balance"]
    table = "accounts"

    def __init__(self):
        self.pk = None
        self.username = None
        self.origpassword=None
        self.password_hash = None
        self.api_key=None
        self.balance = None

    def set_password(self, password):
        self.password_hash = hash_pass(password)

    def set_apikey(self):
        #self.api_key=random.randint(0, 1000)
        self.api_key=''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])

    @classmethod
    def login(cls, username, password):
        account = cls.select_one("WHERE password_hash = ? AND username = ?", (hash_pass(password), username))
        if not account:
            return None
        else:
            return account

    @classmethod
    def api_authenticate(cls,apikey):
        account=cls.select_one("WHERE api_key=?",(apikey,))
        if not account:
            return None
        else:
            return account

    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("cannot make negative deposit")
        self.balance += amount
        self.save()


    def get_positions(self):
        """ return a list of each Position object for this user """
        where = "WHERE account_pk = ?"
        values = (self.pk, )
        return Position.select_many(where, values)

    def get_trades(self):
        """ return a list of all Trades for this user """
        where="WHERE account_pk=?"
        values=(self.pk,)
        return Trade.select_many(where,values)

    def get_trades_for(self, symbol):
        """ return a list of all Trades for a given symbol for this user """
        where="WHERE account_pk=? and ticker=?"
        values=(self.pk,symbol)
        return Trade.select_one(where,values)

    def get_position_for(self,symbol):
        where="WHERE account_pk=? and ticker=?"
        values=(self.pk,symbol)
        result=Position.select_one(where,values)
        if result:
            return result
        position=Position()
        position.account_pk=self.pk
        position.ticker=symbol
        position.shares=0
        return position

    def buy(self,symbol,amount):
        price=get_price(symbol)        
        if self.balance<price*amount:
            raise ValueError("You do not have enough money for this stock")
            
        self.balance-=price*amount
        trade=Trade()
        trade.account_pk=self.pk
        trade.ticker=symbol
        trade.price=price
        trade.volume=amount
        trade.time=time.time()
        position=self.get_position_for(symbol)
        position.shares+=amount

        self.save()   
        trade.save()        
        position.save()

    def sell(self, ticker, amount):
        price = get_price(ticker)
        position = self.get_position_for(ticker)
        if position.shares < amount:
            raise ValueError("Insufficient Shares to Sell or Position Does not Exist")
        self.balance += price * amount
        trade = Trade()
        trade.account_pk = self.pk
        trade.ticker = ticker
        trade.price = price
        trade.volume = -1 * amount
        trade.time = time.time()

        position.shares -= amount
        self.save()
        trade.save()
        position.save()

    def getallprices(self):
        return get_allprice()

    def getallsearchprices(self,searchby):
        return get_allpricesearch(searchby)

    def getprices(self,symbol):
        return get_price(symbol)

    

        

    # code sell logic
    # Need to sell
    # then need to update table
    # then need to sell to trader
    

    # code sell method for homework
    # code view and controller for homework
    # run.py is your base file



            




