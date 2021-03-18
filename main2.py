import requests
# import json
params = {
    "name": "Keyboard Logitech",
    "price": 89,
    "quantity":1
}
endpoint = 'http://127.0.0.1:4000/products'
headers = {"content-type":"application/json"} 
res = requests.post(url=endpoint, json=params, headers=headers)
# print(json.loads(res.text))
print(res.json())
