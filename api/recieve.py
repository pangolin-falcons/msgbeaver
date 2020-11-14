from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')

def hello_world():
    return 'Hello, World!'

sms = {}

class ReceiveSMS(Resource):
    def put(self, newsms_id):
        sms[newsms_id] = request.form['data']
        return {newsms_id: sms[newsms_id]}

api.add_resource(ReceiveSMS, '/<string:newsms_id>')

if __name__ == '__main__':
    app.run(debug=True)
