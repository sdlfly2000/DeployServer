import os
import zipfile
import socketserver
import logging
from enum import IntEnum

BUFF_SIZE = 512
ZipFile = ""
ZipFileDestination = ""

class DeployAction(socketserver.BaseRequestHandler):
    def handle(self):
        self.logger = logging.getLogger(name="deployLogger")
        self.data = bytearray()
        chunckSize = 0
        try:
            while True:
                tData = self.request.recv(BUFF_SIZE)
                if(chunckSize == 0):
                    chunckSize = int.from_bytes(tData[0:2])
                    self.data.append(tData)
                if (chunckSize == self.data.count):
                    break          
            self.logger.info("Data received: %s" % self.data)
            action = self._ParseAction(self.data)

            # self.request.sendall(self.data.upper())
        except Exception as e:
            print(str(e))

    def _ParseAction(self, data):
        actionByte = data[2]
        if(actionByte == Action.UnZipAction):
            self._UnZipFile(ZipFile, ZipFileDestination)
        elif (actionByte == Action.RestartService):
            self.RestartHostServer()
        else:
            pass

    def _UnZipFile(self, zipFile, destination):
        try:
            if zipfile.is_zipfile(zipFile):
                with zipfile.ZipFile(zipFile, 'r') as zipf:
                    zipf.extractall(destination)
        except Exception as e:
            print(str(e))
        
    def RestartHostServer(self):
        pass

class Action(IntEnum):
    UnZipAction = 1
    RestartService = 2

if __name__ == "__main__":
    pass