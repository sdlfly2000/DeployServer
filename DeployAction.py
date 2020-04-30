import os
import zipfile
import socketserver

class DeployAction(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024)
                print("{} send:".format(self.client_address),self.data)
                if not self.data:
                    print("connection lost")
                    break
                # self.request.sendall(self.data.upper())
        except Exception as e:
            print(str(e))

    def _ParseAction(self, action):
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

if __name__ == "__main__":
    pass