from flask import Flask
from flask_restful import Resource, Api
import device
import chat
import logging

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

class Home(Resource):
    def get(self):
        return "Home page patient medical care chat and device APIs"

class SendMeasurement(Resource):
    def post(self, json_file):
        if device.send_data(json_file):
            logging.info("successful post")
            return "successfully sent measurements"
        else:
            logging.info("post failed")
            return "send measurements failed"

class AddUser(Resource):
    def post(self, first, last, uid):
        return chat.add_user(first, last, uid)

class SendMessage(Resource):
    def post(self, sid, rid, message):
        return chat.send_message(sid, rid, message)

class FetchReceivedMessages(Resource):
    def get(self, first, last):
        return chat.get_messages_received(first, last)

api.add_resource(Home, "/")
api.add_resource(SendMeasurement, "/device/send-measurement/<json_files>")
api.add_resource(AddUser, "/chat/add-user/<first>/<last>/<uid>")
api.add_resource(SendMessage, "/chat/send-message/<sid>/<rid>/<message>")
api.add_resource(FetchReceivedMessages, "/chat/get-messages/<fist>/<last>")

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=80, debug=True)

#host on aws ec2
