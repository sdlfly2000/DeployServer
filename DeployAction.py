import os
import zipfile
import socketserver
import logging
from enum import IntEnum

BUFF_SIZE = 512
ZipFile = "/home/sdlfly2000/Uploads/netcoreapp3.1.zip"
ZipFileDestination = "/home/sdlfly2000/Projects/ImageReceiveService/"

class DeployAction(socketserver.BaseRequestHandler):
    def handle(self):
        self.logger = logging.getLogger(name="deployLogger")
        self.data = []
        chunckSize = 0
        try:
            while True:
                tData = self.request.recv(BUFF_SIZE)
                if(chunckSize == 0):
                    chunckSize = int.from_bytes(tData[0:2], byteorder='big')
                    for data in tData:
                        self.data.append(data)
                if (chunckSize == len(self.data)):
                    break          
            self.logger.info("Data received: %s" % self.data)
            self._ParseAction(self.data)

            # self.request.sendall(self.data.upper())
        except Exception as e:
            self.logger.info(str(e))

    def _ParseAction(self, data):
        actionByte = data[2]
        if(actionByte == Action.UnZipAction):
            self._UnZipFile(ZipFile, ZipFileDestination)
        elif (actionByte == Action.RestartService):
            self._RestartHostServer()
        else:
            pass

    def _UnZipFile(self, zipFile, destination):
        try:
            self.logger.info("Unzip ZipFile: %s" % zipFile)
            self.logger.info("Unzip Destination: %s" % destination)
            if zipfile.is_zipfile(zipFile):
                with zipfile.ZipFile(zipFile, 'r') as zipf:
                    zipf.extractall(destination)
        except Exception as e:
            self.logger.info(str(e))
        
    def _RestartHostServer(self):
        os.system("echo %s | sudo -S %s" % ("sdl@1215", "service supervisor restart"))

class Action(IntEnum):
    UnZipAction = 1
    RestartService = 2

if __name__ == "__main__":
    pass