import PaytmChecksum
import config

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def app_create():
    data = config.getTransactionToken(name=config.name,amount= config.amount)
    print(data)
    amount = data['amount']
    orderid = data['orderId']
    token = data['txnToken']
    print(amount,orderid,token)
    return render_template('index.html',amount=amount,orderid=orderid,token=token, mid=config.PAYTM_MID,env=config.PAYTM_ENVIRONMENT,data=data)

if __name__ == '__main__':
    app.run()