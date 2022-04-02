from Utils.communication import getLocation, getMessages
from flask import Flask
from flask_restful import Resource, Api

distances = [100.0, 115.5, 142.7]

messages = [["este", "", "", "mensaje", ""], ["", "es", "", "", "secreto"], ["este", "", "un", "", ""]]

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)

getLocation(distances)

getMessages(messages)