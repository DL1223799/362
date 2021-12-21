import json


items = {"items":[ {
            "id":0,
            "name":"apple",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":1,
            "name":"orange",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":2,
            "name":"pineapple",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":3,
            "name":"mango",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":4,
            "name":"watermelon",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":5,
            "name":"strawberry",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":6,
            "name":"banana",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":7,
            "name":"pomegranates",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":8,
            "name":"grapes",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        },
        {
            "id":9,
            "name":"papaya",
            "description":"a fruit",
            "price":"123",
            "quantity":5
        }
 ]    
}

FILENAME = "product.json"
with open(FILENAME, "w") as file:
    json.dump(items, file, indent=4)
with open(FILENAME) as file:
    load_data = json.load(file)



print(load_data["items"][0])


