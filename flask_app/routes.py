from flask import jsonify,request
from flask_app import app
from app import util
from app import Account


UNAUTHORIZED={"error:":"unauthorized","STATUS CODE":400}
NOTFOUND={"error:":"NOT FOUND","STATUS CODE":404}
APPERROR={"error:":"APPLICATION ERROR","STATUS CODE":500}
BADREQUEST={"error:":"BAD REQUEST","STATUS CODE":400}

@app.errorhandler(404)
def error404(e):
    return jsonify(NOTFOUND),404

@app.errorhandler(500)
def error500(e):
    return jsonify(APPERROR),500

@app.route('/')
def root():    
    return jsonify({"name":"API Trader"})

@app.route('/api/price/<ticker>')
def price(ticker):
    
    price=util.get_price(ticker)
    if price==False:
        return jsonify(NOTFOUND),404
        
    
        
    return jsonify({"ticker":ticker,"price":price})

@app.route('/api/<api_key>/balance')
def balance(api_key):
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    return jsonify({"username": account.username,"balance":account.balance})

@app.route('/api/<api_key>/positions')
def positions(api_key):
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    positions=account.get_positions()        
    json_list=[position.json() for position in positions]
    return jsonify({"username": account.username,"positions":json_list})

@app.route('/api/<api_key>/deposit',methods=['PUT'])
def deposit(api_key):
    if not request.json or 'amount' not in request.json:
        return jsonify(BADREQUEST),400
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    amount=request.json['amount']
    
    account.deposit(float(amount))
    account.save()
    return jsonify({"username": account.username,"balance":account.balance})

@app.route('/api/<api_key>/trades')
def trades(api_key):
    account=Account.api_authenticate(api_key)    
    if not account:
        return jsonify(UNAUTHORIZED),401
    
    t=account.get_trades()
    json_list=[trade.json() for trade in t]
    return jsonify({"username": account.username,"trades":json_list})

@app.route('/api/<api_key>/sell',methods=['PUT'])
def sell(api_key):
    if not request.json or 'amount' not in request.json or 'ticker' not in request.json:
        return jsonify(BADREQUEST),400
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    amount=request.json['amount']
    symbol=request.json['ticker']
    if int(amount)<0:
        return jsonify(BADREQUEST),400
    account.sell(symbol,int(amount))
    account.save()
    return jsonify({"username": account.username,"shares":amount,"ticker":symbol,"balance":account.balance})

@app.route('/api/<api_key>/buy',methods=['PUT'])
def buy(api_key):
    if not request.json or 'amount' not in request.json or 'ticker' not in request.json:
        return jsonify(BADREQUEST),400
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    amount=request.json['amount']
    symbol=request.json['ticker']
    if int(amount)<0:
        return jsonify(BADREQUEST),400
    account.buy(symbol,int(amount))
    account.save()
    return jsonify({"username": account.username,"shares":amount,"ticker":symbol,"balance":account.balance})

@app.route('/api/<api_key>/stocks/viewall')
def viewall(api_key):
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    stocks=account.getallprices()
    if stocks==False:
        return jsonify(NOTFOUND),404
    json_list=[allstocks for allstocks in stocks]    
    return jsonify({"username": account.username,"stocks":json_list})

@app.route('/api/createaccount',methods=['PUT'])
def createaccount():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        return jsonify(BADREQUEST),400
    account=Account()
    r=request.json    
    account.username=r['username']
    account.set_password(r['password'])
    account.set_apikey()
    account.balance=0.00    
    account.save()
    return jsonify({"username": account.username,"apikey":account.api_key})

@app.route('/api/viewapikey',methods=['POST'])
def viewapikey():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        print(request.json)
        return jsonify(BADREQUEST),400
    
    r=request.json
    account=Account.login(r['username'],r['password'])    
    return jsonify({"username": account.username,"apikey":account.api_key})

@app.route('/api/<api_key>/stocks/searchall/<search>')
def searchall(api_key,search):
    account=Account.api_authenticate(api_key)
    if not account:
        return jsonify(UNAUTHORIZED),401
    stocks=account.getallsearchprices(search)
    
    if stocks==False:
        #stocks=account.getallprices()
        return jsonify(NOTFOUND),404
    json_list=[allstocks for allstocks in stocks]    
    return jsonify({"username": account.username,"stocks":json_list})