import requests

data = {
    "reports": 0,
    "share": 0.245,
    "expenditure": 3.438,
    "owner": "yes"
       }

url = "http://127.0.0.1:9696/predict"
response = requests.post(url, json=data)#.json())
print(response.json())

