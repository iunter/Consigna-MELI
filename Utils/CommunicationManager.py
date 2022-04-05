from turtle import position
from Utils.math import trilateration
from Clases.satellite import Satellite


#Creating Satellites
kenobi = Satellite("Kenobi", -500.0, -200.0)
skywalker = Satellite("Skywalker", 100.0, -100.0)
sato = Satellite("Sato", 500.0, 100.0)
satellites = [kenobi, skywalker, sato]

class CommunicationManager:
    
    def __init__(self) :
        self.satellitesInUse = satellites
        self.communications = []
    
    def getLocation(self, distances):
        
        if len(self.satellitesInUse) < 3:
            return []
        
        #The trilateration algorithm needs a Z coordinate, in this case it is 0
        firstCoordinates = [self.satellitesInUse[0].xPosition, self.satellitesInUse[0].yPosition, 0]
        secondCoordinates = [self.satellitesInUse[1].xPosition, self.satellitesInUse[1].yPosition, 0]
        thirdCoordinates = [self.satellitesInUse[2].xPosition, self.satellitesInUse[2].yPosition, 0]
        
        if len(distances) < 3 :
            return []
        
        #Both the satellites and their distances are given in the same order
        return trilateration(firstCoordinates, secondCoordinates, thirdCoordinates, distances)
        
    def getMessages(self, messages):
        
        if len(messages) == 0:
            return None
        
        messageSize = len(messages[0])
        finalMessage = [""] * messageSize
        for message in messages:
            for index, word in enumerate(message):
                if word:
                    finalMessage[index] = word
        
        if "" in finalMessage:
            return None
            
        return finalMessage
    
    def getLocationAndMessages(self):
        
        distances = []
        messages = []
        orderedSattelites = []
        
        for comm in self.communications:
            orderedSattelites.append(comm.satellite)
            distances.append(comm.distance)
            messages.append(comm.message)
        
        self.satellitesInUse = orderedSattelites
                    
        position = self.getLocation(distances)
        message = self.getMessages(messages)
                
        return position,message
    
    def findSatellite(self, satelliteName):
        requestedSatellite = None
        
        for satellite in satellites:
            if satellite.name.lower() == satelliteName.lower():
                requestedSatellite = satellite
                
        return requestedSatellite
    
    def addCommWithSatellite(self, newComm):
        
        position = -1
        
        for index, comm in enumerate(self.communications):
            if comm.satellite.name == newComm.satellite.name:
                position = index
        
        if position != -1:
            self.communications[position] = newComm
        else:
            self.communications.append(newComm)
            
    
    def purge(self):
        
        self.satellitesInUse = []
        self.communications = []

            