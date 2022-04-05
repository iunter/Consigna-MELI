from flask_restful import Resource, request
from flask import abort
import ast
from Clases.CommWithSatellite import CommWithSatellite
from Utils.CommunicationManager import CommunicationManager
from Utils.strings import listToString

communication = CommunicationManager()


def validateMessageAndDistanceInput(messageInput, distanceInput):
        if type(messageInput) is not list:
            abort(400, "Message is not a list")
        
        if not isinstance(distanceInput, (int, float, complex)) or isinstance(distanceInput, bool):
            abort(400, "Distance given is not a number")

def getBody():
        data = request.data.decode("utf-8")
        filtered_characters = list(s for s in data if s.isprintable())
        filtered_string = ''.join(filtered_characters).replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
        returnData = None
        try:
            returnData = ast.literal_eval(filtered_string)
        except:
            abort(400, "Could not read data")
        return returnData


class TopSecret(Resource):
    
    def post(self):        
        satellites = []
        distances = []
        messages = []
        
        body = getBody()
        
        if 'satellites' not in body:
            abort(400, "Could not read data")
            
        if type(body['satellites']) is not list:
            abort(400, "Satellites list expected")
        
        for satellite in body['satellites']:
            satelliteName = communication.findSatellite(satellite['name'])
            
            #If the satellite have not been found
            if satelliteName == None:
                abort(404, "Could not find satellite: " + satellite['name'])   
            validateMessageAndDistanceInput(satellite['message'], satellite['distance'])             
            satellites.append(satelliteName)
            distances.append(satellite['distance'])
            messages.append(satellite['message'])
                
                
        communication.satellitesInUse = satellites
        
        position = communication.getLocation(distances)
        message = communication.getMessages(messages)
        
        communication.purge()
        
        if message == None:
            abort(404, "Could not determine the message")
            
        if len(position) == 0:
            abort(404, "Could not determine position")
                        
        return {
            'position' : { 
                'x' : position[0],
                'y' : position[1]
                },
            'message' : listToString(message)
            }
        

class TopSecretSplit(Resource):
    
    def post(self, satelliteName):
        
        body = getBody()
        
        satellite = communication.findSatellite(satelliteName)
        
        if satellite == None:
            abort(404, "Could not find satellite: " + satelliteName)
            
        messageInput = body['message']
        distanceInput = body['distance']
            
        validateMessageAndDistanceInput(messageInput, distanceInput)
            
        communication.addCommWithSatellite(CommWithSatellite(satellite, distanceInput, messageInput))       
                
        return "Communication with satellite: " + satelliteName.upper() + " succesfully added"
    
    def get(self, satelliteName=None):
        
        position, message = communication.getLocationAndMessages()
        
        communication.purge()
        
        if len(position) == 0:
            abort(404, "Could not determine position")
            
        if message == None:
            abort(404, "Could not determine the message")
        
        return  {
            'position' : { 
                'x' : position[0],
                'y' : position[1]
                },
            'message' : listToString(message)
            }