from flask import Flask
from flask_restful import Resource, Api
from Restful.TopSecret import TopSecret, TopSecretSplit

app = Flask(__name__)
api = Api(app)

class FrontPage(Resource):
    def get(self):
        return "Api is up and running :)"

api.add_resource(FrontPage, '/')
api.add_resource(TopSecret, '/topsecret')
api.add_resource(TopSecretSplit, '/topsecret_split/<satelliteName>')

if __name__ == '__main__':
    app.run(debug=True)