from Utils.math import trilateration
from Clases.satellite import Satellite
from Clases.message import SatelliteCommunication


#Creating Satellites
kenobi = Satellite("Kenobi", -500.0, -200.0)
skywalker = Satellite("Skywalker", 100.0, -100.0)
sato = Satellite("Sato", 500.0, 100.0)
satellites = [kenobi, skywalker, sato]

#Creating Communication with Satellite
kenobiComm = SatelliteCommunication(kenobi, 100.0, ["este", "", "", "mensaje", ""])
skywalkerComm = SatelliteCommunication(skywalker, 115.5, ["", "es", "", "", "secreto"])
satoComm = SatelliteCommunication(sato, 142.7, ["este", "", "un", "", ""])
communications = [kenobiComm, skywalkerComm, satoComm]

class Communication:
    
    def __init__(self) :
        self.satellites = satellites
        self.communications = communications
    
    def getLocation(self, distances):
        #Assuming the distances are given in the following order (kenobi, skywalker, sato)
        #The trilateration algorithm needs a Z coordinate, in this case it is 0
        firstCoordinates = [kenobi.xPosition, kenobi.yPosition, 0]
        secondCoordinates = [skywalker.xPosition, skywalker.yPosition, 0]
        thirdCoordinates = [sato.xPosition, sato.yPosition, 0]
        
        return trilateration(firstCoordinates, secondCoordinates, thirdCoordinates, distances)
        
    def getMessages(self, messages):
        messageSize = len(messages[0])
        finalMessage = [""] * messageSize
        for message in messages:
            for index, word in enumerate(message):
                if word:
                    finalMessage[index] = word
        
        if "" in finalMessage:
            finalMessage = "Could not determine message"
            
        return finalMessage
    
    def findSatellite(self, satelliteName):
        requestedSatellite = "Could not find satellite"
        
        for satellite in self.satellites:
            if satellite.name.lower() == satelliteName.lower():
                requestedSatellite = satellite
                
        return requestedSatellite
            