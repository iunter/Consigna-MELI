from flask_restful import Resource, request, reqparse
import json
import ast
from Utils.communication import Communication
from Utils.strings import listToString

parser = reqparse.RequestParser()
parser.add_argument('hola', type=str)

class TopSecret(Resource):
    
    def post(self):
        communication = Communication()
        satellites = []
        distances = []
        messages = []
        data = request.data.decode("utf-8")
        filtered_characters = list(s for s in data if s.isprintable())
        filtered_string = ''.join(filtered_characters).replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        a = ast.literal_eval(filtered_string)
        
        for satellite in a['satellites']:
            satellites.append(communication.findSatellite(satellite['name']))
            distances.append(satellite['distance'])
            messages.append(satellite['message'])
            
        communication.satellites = satellites
        
        position = communication.getLocation(distances)
        message = communication.getMessages(messages)
        
        print(position[0])
        
        return {
            'position' : { 
                'x' : position[0],
                'y' : position[1]
                },
            'message' : listToString(message)
            }