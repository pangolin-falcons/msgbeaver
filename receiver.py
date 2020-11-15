from flask import Flask, request
from store import Store
from dispatcher import Dispatcher
import requests
import json

app = Flask(__name__)

def msg_process(msg, tstamp):
    js = json.loads(msg)
    storeData = Store()
    storeData.storeRequest(js['originationNumber'], js['messageBody'])
    print("Passed to store")
    d = Dispatcher(js['originationNumber'], js['messageBody'])
    print("Dispatcher Generated")

@app.route('/', methods = ['GET', 'POST', 'PUT'])
def sns():
    try:
        js = json.loads(request.data)

        hdr = request.headers.get('X-Amz-Sns-Message-Type')
        # subscribe to the SNS topic
        if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
            r = requests.get(js['SubscribeURL'])

        if hdr == 'Notification':
            msg_process(js['Message'], js['Timestamp'])

    except:
        pass

    return 'OK\n'

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 8000,
        debug = True
    )
