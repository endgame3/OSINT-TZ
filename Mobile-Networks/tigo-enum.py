from urllib import response
import requests
import json
import pdb
import pandas as pd

headers = {
    "Content-Type": "application/json",
    "User-Agent": "PESA/8 CFNetwork/978.0.7 Darwin/18.7.0",
    "Accept-Language": "en-us",
}

url = "https://accessgw.tigo.co.tz:7443"

def convert_data(data):
    return json.dumps(data)


def get_info(num):
    endpoint = url + "/tigoagentapp_engrafilive?featureId=register.new.customer.view.web"
    data = {
        "idProofNumber":"",
        "customerMsisdn":f"{num}",
        "perPageCount": "10",
        "SessionToken": "tigo_sess_b5999295b2d5e43190d2e9a4b528e13f",
        "isMobileRequest":False,
        "isLegacyData":True,
        "retailerId":"0",
        "pageNo":"1",
        "isTemporaryDetails":False
    }
    data = convert_data(data)
    r = requests.post(endpoint, headers=headers, data=data, verify=False)
    response = r.json()
    print(response['respData'])

num = input("Enter number : ")
get_info(num)
