import os
import time
def mainview():
    print("Welcome to StellarDimensions Terminal Trading Application\n")
    print("Please choose from one of the options below: ")
    print(" 1. Create an Account\n 2. Login to your Account\n 3. Quit\n")
    print("Enter Selection: ",end='')

def enter_user_name():
    print("Enter User Name: ",end='')

def enter_password():
    print("Enter password: ",end='')

def enter_deposit():
    print("Enter Deposit: ",end='')

def enter_symbol():
    print("Enter Symbol: ",end='')

def enter_amount():
    print("Enter Amount: ",end='')

def sell_message():
    print("\nPlease enter the information to sell your stock")

def main_quit():
    print("Thank You for trading with StellarDimensions Terminal Trader!")

def buy_success_message(symbol,amount,balance,sharecost):
    print("\nYou purchased {0} shares of symbol {1} for the amount of ${2:.2f}. Your remaining balance is: ${3:.2f}".format(int(amount),str(symbol),sharecost,balance))

def sell_success_message(symbol,amount,balance):
    print("\nYou sold {0} shares of symbol {1}.Your remaining balance is: ${2:.2f}".format(int(amount),str(symbol),balance))

def account_success_message():
    print("\nAccount created Succesfully!")

def login_failed_message():
    print("Login failed!. Returning to main menu")

def deposit_success_message(newdeposit):
    print("\nDeposit successfull")
    print("Your New Balance is: "+str(newdeposit))

def invalid_symbol_message():
    print("You need to have at least enter 1 character to list stock options!")

def insufficient_funds_message():
    print("You do not have enough money")

def insufficient_shares_message():
    print("You do not have enough shares")

def show_stock_price(symbol,stockprice):
    print("The price of stock {0} per share is ${1:.2f} in US Currency.".format(symbol,stockprice))
    

def show_stock_list(stocklist,lookupvalue):
    print("Preview all prices below") 
    for np in stocklist:
        if len(lookupvalue)==1:
            if str(np).startswith(lookupvalue,8,9):
                print(str(np))
                break                
        elif len(lookupvalue)>1:
            if str(np).startswith(lookupvalue,8):
                print(str(np))
                time.sleep(1)

def show_api_key(apikey):
    print("This is your api key {}".format(apikey))
            

def loginview():
    print("Welcome to StellarDimensions Terminal Trading Application\n")    
    print("Please choose from one of the options below: ")
    print(" 1. Make Deposit\n 2. List Stocks\n 3. View Stock Price\n 4. Buy Shares\n 5. Sell Shares\n 6. View API Key\n 7. Return to Main Menu\n")
    print("Enter Selection: ",end='')




