import requests
import json
import pdb
import pandas as pd


headers = {
    "Content-Type": "application/json",
    "User-Agent": "GePG Tanzania/15 CFNetwork/978.0.7 Darwin/18.7.0",
    "Accept-Language": "en-us",
}

url = "http://app.gepg.go.tz:8006"

def convert_data(data):
    return json.dumps(data)

def get_last_tokens(num):
    endpoint = url + "/api/last-token"
    data = {
        "meter":"",
        "deptCellNum":f"{num}",
        "pspReceipt":"",
        "gepgReceipt":""
    }
    data = convert_data(data)
    r = requests.post(endpoint, headers=headers, data=data)
    print(r.json())

num = input("Enter the number : ")
get_last_tokens(num)
