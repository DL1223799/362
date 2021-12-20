import server
import json
from urllib.request import Request, urlopen
# query 

SERVER = "localhost:5000"
JSON_CONTENT_TYPE = "application/json; charset=UTF-8"

def query(name):
    data = {"name":name}
    req = Request(url = f"http://{SERVER}/query/{data}",
    data = json.dumps(data).encode("utf-8"),
    )

