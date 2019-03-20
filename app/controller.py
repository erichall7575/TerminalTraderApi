import getpass
import os
from app import view
from app import util
from app.account import Account


def run():
    account=login_menu()
    if not account:
        return None
    
def make_deposit(account):
    view.enter_deposit()
    depositinfo=input()
    depositinfo=float(depositinfo)
    account.deposit(depositinfo)
    view.deposit_success_message(account.balance)
    return main_menu(account)

def list_stocks(account):
    view.enter_symbol()
    symbol=input()
    if len(symbol)>=1:
        view.show_stock_list(account.getallprices(),str(symbol).upper())        
    elif len(symbol)<1:
        view.invalid_symbol_message()
    return main_menu(account)  
      
def buy_stocks(account):
    try:               
        view.enter_symbol()
        symbol=input()
        view.enter_amount()
        amount=input()
        amount=float(amount)
        account.buy(str(symbol).upper(),amount)
        sharecost=util.get_price(symbol)*amount        
        view.buy_success_message(str(symbol).upper(),amount,account.balance,sharecost)
    except ValueError:
        view.insufficient_funds_message()
    return main_menu(account)

def sell_stocks(account):
    try:
        view.sell_message()
        view.enter_symbol()
        symbol=input()
        view.enter_amount()
        amount=input()
        amount=float(amount)
        account.sell(str(symbol).upper(),amount)
        view.sell_success_message(str(symbol).upper(),amount,account.balance)
    except ValueError:
        view.insufficient_shares_message()

    return main_menu(account)

def view_stocks(account):
    view.enter_symbol()
    symbol=input()
    view.show_stock_price(str(symbol).upper(),account.getprices(str(symbol).upper()))
    return main_menu(account)

def view_apikey(account):
    view.show_api_key(account.api_key)
    return main_menu(account)


def main_menu(account):
    while True:               
        view.loginview()
        mainselect=input()
        if mainselect=='1':
            return make_deposit(account)
            
        if mainselect=='2':
            return list_stocks(account)

        if mainselect=='3':
            return view_stocks(account)
                            
        if mainselect=='4': 
            return buy_stocks(account)

        if mainselect=='5':
            return sell_stocks(account)

        if mainselect=='6':
            return view_apikey(account)

        if mainselect=='7':
            return login_menu()
                            


       
            
def login_account():
    loginaccount=Account()                        
    view.enter_user_name()
    username=input()
    view.enter_password()
    password=getpass.getpass()           
    enteraccount=loginaccount.login(username,password)
    if enteraccount is None:
        view.login_failed_message()
        return login_menu()
    elif enteraccount is not None:            
        return main_menu(enteraccount)        
        
def create_account_selection():
    while True:
        newuser=Account()
        view.enter_user_name()
        username=input()
        newuser.username=username
        view.enter_password()
        password=getpass.getpass()
        newuser.origpassword=password
        newuser.set_password(password)
        #newuser.apikey=20
        newuser.set_apikey()        
        newuser.balance=0.00
        newuser.save()
        view.account_success_message()
        return newuser

def login_menu():
    while True:
        view.mainview()
        mainselect=input()
        if mainselect=='3': 
            view.main_quit()           
            break
        if mainselect=='1':
            newacc=create_account_selection()            
            return main_menu(newacc)            

        if mainselect=='2':            
            return login_account()
            
                
            

    




            





            
            
    
