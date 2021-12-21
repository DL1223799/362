# import server
import json
from urllib.request import Request, urlopen
# query 

SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

def queryP(name):
    queryname = {"name":name}
    with urlopen(f"http://{SERVER}/query/{queryname}") as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result

def buyP(name,quantity):
    queryname = {"name":name}
    buyQuan = {"quantity":quantity}
    with urlopen(f"http://{SERVER}/buy/{queryname}/{buyQuan}") as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result
def replenishP(name,quantity):
    queryname = {"name":name}
    replenishQuan = {"quantity":quantity}
    with urlopen(f"http://{SERVER}/buy/{queryname}/{replenishQuan}") as resp:
        result = json.load(resp.read().decode("utf-8"))
    return result