import imp
from Utils.communication import Communication
from flask import Flask
from flask_restful import Resource, Api
from Restful.TopSecret import TopSecret
distances = [100.0, 115.5, 142.7]

messages = [["este", "", "", "mensaje", ""], ["", "es", "", "", "secreto"], ["este", "", "un", "", ""]]

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'camuchis'}

api.add_resource(HelloWorld, '/')
api.add_resource(TopSecret, '/topsecret')

if __name__ == '__main__':
    app.run(debug=True)

#getLocation(distances)

#getMessages(messages)