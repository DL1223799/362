# import server
import json
from logging import exception
from urllib.request import Request, urlopen
# query 

SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

def queryP(id):
    queryId = {"id":id}
    req = Request(url = f"http://{SERVER}/api/query",
        
        headers = {"Content-type": JSON_CONTENT_TYPE},
        method = "GET")
    with urlopen(req) as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result

def buyP(id,quantity,creditCard):
    id = {"id":id}
    buyQuan = {"quantity":quantity}
    req = Request(url = f"http://{SERVER}/api/buy",
        
        headers = {"Content-type": JSON_CONTENT_TYPE},
        method = "GET")
    with urlopen(f"http://{SERVER}/api/buy/") as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result

def replenishP(id,quantity):
    queryId = {"name":id}
    replenishQuan = {"quantity":quantity}
    req = Request(url = f"http://{SERVER}/api/replenish",
        
        headers = {"Content-type": JSON_CONTENT_TYPE},
        method = "GET")
    with urlopen(f"http://{SERVER}/api/replenish/") as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result