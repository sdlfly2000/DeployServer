import os
import zipfile
import socketserver
import logging
from enum import IntEnum

BUFF_SIZE = 512
ZipFile = "/home/sdlfly2000/Uploads/netcoreapp3.1.zip"
ZipFileDestination = "/home/sdlfly2000/Projects/ImageReceiveService/"

class DeployRequest():
    def __init__(self, recvData: bytes):
        self.recvData = recvData
        self.RequestLength = self.__GetRequestLength(recvData)
        self.RequestCommandCode = self.__GetCommandCode(recvData)

    def __GetRequestLength(self, data: bytes) -> int:
        return int.from_bytes(data[0:2], byteorder='big') if len(data) > 0 else None
        
    def __GetCommandCode(self, data: bytes) -> int:
        return data[2] if len(data) > 2 else None

class Action(IntEnum):
    UnZipAction = 1
    RestartService = 2

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