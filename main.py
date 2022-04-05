from flask import Flask
from flask_restful import Resource, Api
from Restful.TopSecret import TopSecret, TopSecretSplit

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'camuchis'}

api.add_resource(HelloWorld, '/')
api.add_resource(TopSecret, '/topsecret')
api.add_resource(TopSecretSplit, '/topsecret_split/<satelliteName>')

if __name__ == '__main__':
    app.run(debug=True)

#getLocation(distances)

#getMessages(messages)