from itertools import product
import json
from os import lockf
from flask import Flask,jsonify,request,Response
from flask_sqlalchemy import SQLAlchemy
# import client
import hashlib
import socket,sys,threading,unittest
import json


SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

app = Flask(__name__)
exe_id = ""

HOST = "time-b-b.nist.gov"
PORT = 13
lock = threading.Lock()

class itemx():
    def get_one_item(id,desc,price,quantity):
        return jsonify(
                {"exe_id":obtain(),
                "id":id,
                "desc":desc,
                "price":price,
                "quantity":quantity},200)

def obtain():
    global HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        time = sock.recv(1024)
    time = time.decode("utf-8").strip()
    exe_id = hashlib.sha256(time.encode("utf-8")).hexdigest()
    return exe_id


def readjson():
    with open("product.json","r") as prodfile:
        info = prodfile.dumps()
    print(info)

def checkId(id):

    for i,item in enumerate(items["items"]):
        if i["item"]["id"] == id:
            
            return True
    return False

def checkQty(quantity):
    if i["item"]["quantity"] >= quantity:
        return True
    else: return False

def checkCredit(creditCard):
    if creditCard.length() >=16:
        return True
    else: return False

@app.route("/api/query/<int:id>")#,methods=["POST"]
def query(id):
    data = json.loads("product.json")
    id = data.get("id")
    for item in data["items"]:
        if item["id"] == id:
            return jsonify({"exe_id": exe_id, "success": True, "result": item}),200     
    return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404


@app.route("/api/buy",methods =["GET"])
def buy():
    global lock
    try:
        data = json.loads(request.data)
        if "id" in data:
            id = data.get("id")
        if "quantity" in data:
            quantity = data.get("quantity")
        if "creditCardNo" in data:
            creditCardNo = data.get("creditCardNo")
        

        if (checkId(id)==True and checkQty(quantity)== True and checkCredit(creditCardNo)==True):
            data = json.loads("product.json")
            for items in data["items"]:
                if items["id"] == id:
                    items["quantity"] -= quantity
                    json.dump("product.json",data,indent=4)
                    return {"exe_id": exe_id, "success": True, "result": f"The total price: {items['price']*quantity}"}
            
        elif (checkId(id)==False): return jsonify({"exe_id": exe_id,"error": "Credit card invalid"}), 404
        elif (checkQty(quantity)==False): return jsonify({"exe_id": exe_id,"error": "Stock is not enough"}), 404
        elif (checkCredit(creditCardNo)==False): return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404
    except:
        

@app.route("/api/replenish/",methods=["GET"])
def replenish():
    data = json.loads("product.json")
    id = data.get("id")
    quantityAdd = data.get("quantity")
    creditCard = data.get()
    for i,item in enumerate(items):
        if items["id"] == id:
            items["quantity"] += quantityAdd
            return {"exe_id": exe_id, "success": True, "result": item}
        else: return jsonify({"exe_id":exe_id,"error": "todo item not found"}), 404


if __name__ == "__main__":
    a_string = obtain()
    # exe_id = hashlib.sha256(a_string.encode("utf-8")).hexdigest()  
    print(obtain)
    app.run()
    app.readjson()
    