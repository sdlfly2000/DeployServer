import socket               

if __name__ == "__main__":
    s = socket.socket()         
    host = socket.gethostname() 
    port = 4001                
    
    s.connect((host, port))
    s.send("Hello".encode())
    s.close()