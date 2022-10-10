import requests

url = "http://localhost:9696/predict"
client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
print (requests.post(url, json=client).json())

