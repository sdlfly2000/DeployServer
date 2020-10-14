class DeployRequest():
    def __init__(self, recvData: bytes):
        self.recvData = recvData
        self.RequestLength = self.__GetRequestLength(recvData)
        self.RequestCommandCode = self.__GetCommandCode(recvData)

    def __GetRequestLength(self, data: bytes) -> int:
        return int.from_bytes(data[0:2], byteorder='big') if len(data) > 0 else None
        
    def __GetCommandCode(self, data: bytes) -> int:
        return data[2] if len(data) > 2 else None