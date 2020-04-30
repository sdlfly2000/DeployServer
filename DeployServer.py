import os
import socketserver
from DeployAction import DeployAction

class Deployment():
    def __init__(self):
        self.MonitorPort = 4001
        self.hostName = socketserver.socket.gethostname()
        self.server = self._CreateServer(self.hostName, self.MonitorPort)
    
    def StartMonitor(self):
        self.server.serve_forever()

    def StopMonitor(self):
        self.server.shutdown()

    def _CreateServer(self, host, port):
        return socketserver.TCPServer((host, port), DeployAction)


if __name__ == "__main__":
        server = Deployment()
        server.StartMonitor()


