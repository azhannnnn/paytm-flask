import requests
import json
import PaytmChecksum
import datetime

PAYTM_MID = "216820000000000077910"
PAYTM_MERCHANT_KEY = "QU%rHGbkHQB%H%OY"
PAYTM_ENVIRONMENT= 'https://router.paytm.in'
PAYTM_WEBSITE= 'DEFAULT'

name="Azhan"
amount= '1.00'

def getTransactionToken(name,amount):
    payment_data = {
        "name": name,  # Replace with customer's name
        "amount": amount     # Use the amount received from the API response
    }
    print(payment_data)
    response = requests.post("http://13.127.81.177:8000/pay/", json=payment_data)
    print(response.json())
    if response.status_code == 200:
        payment_info = response.json()
        if payment_info.get("txnToken"):
            return payment_info
    return ""