import socket               

if __name__ == "__main__":
    s = socket.socket()         
    host = socket.gethostname() 
    # host = "182.61.37.221"
    port = 4002                
    
    # Message to restart supervisor on server
    data = [0x00, 0x03, 0x02] 
    
    s.connect((host, port))
    s.send(bytes(data))
    s.close()