import socket               

if __name__ == "__main__":
    s = socket.socket()         
    host = socket.gethostname() 
    # host = "182.61.37.221"
    port = 4001                
    
    data = [0x00, 0x03, 0x01]
    
    s.connect((host, port))
    s.send(bytes(data))
    s.close()