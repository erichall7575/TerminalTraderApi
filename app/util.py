import requests
import hashlib

ENDPOINT = "https://api.iextrading.com/1.0"
CALL = "/stock/{symbol}/price"
SYMBOLS="https://api.iextrading.com/1.0/ref-data/symbols"
salt = "its a secret to everyone"


def hash_pass(password):
    # salted 128 character hash of a string
    hasher = hashlib.sha512()
    value = password.encode() + salt.encode()
    
    hasher.update(value)
    return hasher.hexdigest()


def get_price(symbol):
    response = requests.get(ENDPOINT + CALL.format(symbol=symbol))
    if response.status_code == 200:
        return response.json()
    else:
        #raise requests.ConnectionError('http status: ' + format(response.status_code))
        return False

def get_allprice():
    response = requests.get(SYMBOLS)
    if response.status_code == 200:
        pricelist=response.json()
        pricelistname=[]
        # pricelistname=[]
        # for p in pricelist:
        #     pstr="Symbol: {}|Name: {}|Active: {}".format(str(p['symbol']),str(p['name']),str(p['isEnabled']))
        #     pricelistname.append(pstr)        
        for p in pricelist:
            pstr={"ticker":p['symbol'],
                  "stockname":p['name'],
                  "isEnabled":p['isEnabled']}
            pricelistname.append(pstr)    
        return pricelistname
    else:
        #raise requests.ConnectionError('http status: ' + format(response.status_code))
        return False

def get_allpricesearch(searchby):
    response = requests.get(SYMBOLS)
    if response.status_code == 200:
        pricelist=response.json()
        pricelistname=[]
        #newstr=""
        # pricelistname=[]
        # for p in pricelist:
        #     pstr="Symbol: {}|Name: {}|Active: {}".format(str(p['symbol']),str(p['name']),str(p['isEnabled']))
        #     pricelistname.append(pstr)        
        for p in pricelist:
            #newstr=str(p['symbol']).replace('"','*')
            #newstr=str(newstr).strip()
            if str(p['symbol']).startswith(str(searchby).upper()):
                pstr={"ticker":p['symbol'],
                  "stockname":p['name'],
                  "isEnabled":p['isEnabled']}
                pricelistname.append(pstr) 
                #pricelistname.append(str(searchby).upper())              
                     
             
        return pricelistname
    else:
        #raise requests.ConnectionError('http status: ' + format(response.status_code))
        return False
