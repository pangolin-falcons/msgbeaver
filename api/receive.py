from flask import Flask, request
from store import Store
import requests
import json

app = Flask(__name__)

def msg_process(msg, tstamp):
    js = json.loads(msg)
    storeData = Store()
    storeData.storeRequest(js['originationNumber'], js['messageBody'], tstamp)

@app.route('/', methods = ['GET', 'POST', 'PUT'])
def sns():
    try:
        js = json.loads(request.data)
    except:
        pass

    print(js)
    hdr = request.headers.get('X-Amz-Sns-Message-Type')
    # subscribe to the SNS topic
    if hdr == 'SubscriptionConfirmation' and 'SubscribeURL' in js:
        r = requests.get(js['SubscribeURL'])

    if hdr == 'Notification':
        msg_process(js['Message'], js['Timestamp'])

    return 'OK\n'

if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 8000,
        debug = True
    )
