import os
import zipfile
import socketserver
import logging

from Models.Action import Action
from Models.DeployRequest import DeployRequest

BUFF_SIZE = 512
ZipFile = "/home/sdlfly2000/Uploads/netcoreapp3.1.zip"
ZipFileDestination = "/home/sdlfly2000/Projects/ImageReceiveService/"

class DeployAction(socketserver.BaseRequestHandler):
    def handle(self):
        self.logger = logging.getLogger(name="deployLogger")
        try:
            recvData = self.request.recv(BUFF_SIZE)
            request = DeployRequest(recvData)                
            self.__RecordRecvRequest(request)
            self.__ImplementAction(request.RequestCommandCode)
        except Exception as e:
            self.logger.info(str(e))

    def __ImplementAction(self, commandCode):
        if(commandCode == Action.UnZipAction):
            self.__UnZipFile(ZipFile, ZipFileDestination)
        elif (commandCode == Action.RestartService):
            self.__RestartHostServer()
        else:
            pass
    
    def __RecordRecvRequest(self, request: DeployRequest):
        self.logger.info("Data received: %s" % request.recvData)
        self.logger.info("Request Length: %d" % request.RequestLength)
        self.logger.info("Request Command: %d" % request.RequestCommandCode)

    def __UnZipFile(self, zipFile, destination):
        try:
            self.logger.info("Unzip ZipFile: %s" % zipFile)
            self.logger.info("Unzip Destination: %s" % destination)
            if zipfile.is_zipfile(zipFile):
                with zipfile.ZipFile(zipFile, 'r') as zipf:
                    zipf.extractall(destination)
        except Exception as e:
            self.logger.info(str(e))
        
    def __RestartHostServer(self):
        os.system("echo %s | sudo -S %s" % ("sdl@1215", "service supervisor restart"))

if __name__ == "__main__":
    pass