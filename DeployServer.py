import os
import socketserver
import logging
from DeployAction import DeployAction

class Deployment():
    def __init__(self):
        
        self.logger = logging.getLogger(name="deployLogger")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler("deployment.log")
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        self.MonitorPort = 4002
        self.hostName = socketserver.socket.gethostname()
        self.server = self._CreateServer(self.hostName, self.MonitorPort)
    
    def StartMonitor(self):
        self.logger.info("Start Monitor...")
        self.server.serve_forever()

    def StopMonitor(self):
        self.logger.info("Stop Monitor...")
        self.server.shutdown()

    def _CreateServer(self, host, port):
        self.logger.info("Listening at  : %s : %d" % (host, port))
        return socketserver.TCPServer((host, port), DeployAction)

if __name__ == "__main__":
        server = Deployment()
        server.StartMonitor()


