from flask import Flask
from flask_restful import Resource, Api
import system as device
import logging

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return "Home page for device API module"

class SendMeasurement(Resource):
    def post(self, json_file):
        if device.send_data(json_file):
            logging.info("successful post")
            return "successfully sent measurements"
        else:
            logging.info("post failed")
            return "send measurements failed"

api.add_resource(Home, "/")
api.add_resource(SendMeasurement, "/device/send-measurement/<string: file>")

if __name__ == '__main__':
    app.run(debug=True)