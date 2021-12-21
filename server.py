import json
from os import lockf
from flask import Flask,jsonify,request,Response
from flask_sqlalchemy import SQLAlchemy
# import client
import hashlib
import socket,sys,threading,unittest
import json

item = open(request.data)
SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

app = Flask(__name__)
exe_id = ""

HOST = "time-b-b.nist.gov"
PORT = 13
lock = threading.Lock()

# def retrieve():
#     global data1, data2, data3, data4
#     with open(FILENAME) as file:
#         data1, data2, data3, data4 = file.readline(), file.readline(), file.readline(), file.readline()
#         data1, data2, data3, data4 = data1.split(), data2.split(), data3.split(), data4.split()
#     data1, data3, data4 = [int(x) for x in data1], [int(x) for x in data3], [int(x) for x in data4]

def obtain():
    global HOST, PORT
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        time = sock.recv(1024)
    time = time.decode("utf-8").strip()
    exe_id = hashlib.sha256(time.encode("utf-8")).hexdigest()
    return exe_id

# def get_daytime(host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((host, port))
#         data = s.recv(1024)
#     return data.decode('utf-8').strip()


@app.route("/query/<int:id>")#,methods=["POST"]
def query(id):
    data = json.loads(request.data)
    id = data.get("id")
    for i,item in enumerate(id):
        if item["id"] == id:
            return {"exe_id": exe_id, "success": True, "result": item}     
    return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404


@app.route("/buy/<int:id>/<int:quantity>/",method =["POST"])
def buy(id,quantity):
    global lock
    # str(creditCardNo)
    data = json.loads(request.data)
    id = data.get("id")
    quantityBuy = data.get("quantity")
    for i,item in enumerate(items):
        if items["id"] == id:
            if (quantity<=item["quantity"]):
                if (creditCardNo == creditC["id"] ):
                    lock.acquire()
                    finalprice = item["price"]*quantityBuy
                    item["quantity"] -= quantityBuy
                    lock.release()
                    return {"exe_id": exe_id, "success": True, "result": item}
                else:return jsonify({"exe_id": exe_id,"error": "Credit card invalid"}), 404
            else: return jsonify({"exe_id": exe_id,"error": "Stock is not enough"}), 404
        else: return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404

@app.route("/replenish/<int:id>/<int:quantity>",method=["POST"])
def replenish(id,quantity):
    data = json.loads(request.data)
    id = data.get("id")
    quantityAdd = data.get("quantity")
    for i,item in enumerate(items):
        if items["id"] == id:
            items["quantity"] += quantityAdd
            return {"exe_id": exe_id, "success": True, "result": item}
        else: return jsonify({"exe_id":exe_id,"error": "todo item not found"}), 404

@app.route("/api/query/<int:id>")#,methods=["POST"]
def query(id):
    data = json.loads(request.data)
    for i,item in enumerate(items):
        if items["id"] == id:
            return {"exe_id": exe_id, "success": True, "result": item}     
    return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404


@app.route("/api/buy/<int:id>/<int:quantity>/<int:creditCardNo>",method =["POST"])
def buy(id,quantity,creditCardNo):
    data = json.loads(request.data)
    for i,item in enumerate(items):
        if items["id"] == id:
            if (quantity<=item["quantity"]):
                if (creditCardNo):
                    finalprice = item["price"]*quantity
                    item["quantity"] -= quantity
                    return {"exe_id": exe_id, "success": True, "result": item}
                else:return jsonify({"exe_id": exe_id,"error": "Credit card invalid"}), 404
            else: return jsonify({"exe_id": exe_id,"error": "Stock is not enough"}), 404
        else: return jsonify({"exe_id": exe_id,"error": "todo item not found"}), 404

@app.route("/api/replenish/<int:id>/<int:quantity>",method=["POST"])
def replenish(id,quantity):
    data = json.loads(request.data)
    for i,item in enumerate(items):
        if items["id"] == id:
            items["quantity"] += quantity
            return {"exe_id": exe_id, "success": True, "result": item}
        else: return jsonify({"exe_id":exe_id,"error": "todo item not found"}), 404

if __name__ == "__main__":
    a_string = obtain()
    # exe_id = hashlib.sha256(a_string.encode("utf-8")).hexdigest()  
    print(obtain)
    app.run()
    