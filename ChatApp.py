import socket

class Chatapp:
    def __init__(self, message):
        self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 80
        self.server_address = ((self.server,self.port))
        self.s.connect(self.server_address)
        post = "POST"
        self.s.sendall(post.encode())
        check = self.s.recv(4).decode()
        if check == "ACK":
            self.s.sendall(message.encode())
            self.s.close()
        else:
            print("Connection Error")

class Receive:
    def __init__(self):
        # Receive Message
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 80
        self.server_address = (self.server, self.port)
        self.s.connect(self.server_address)
        post = "GET"
        self.s.sendall(post.encode())
        check = self.s.recv(4).decode()
        if check == "ACK":
            data = self.s.recv(2048).decode()
            self.s.close()
            self.data = data
        else:
            print("Connection Error")

    def receive_message(self):
        return self.s.recv(1024).decode()




if __name__ == "__main__": 
   Chatapp("test")
   Receive()


## Setting up Network settings
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#server = "127.0.0.1"
#port = 80
#
## Connecting to the server
#server_address = ((server,port))
#s.connect(server_address)
#
## Send Message
#message = "Hello, World!"
#s.sendall(message.encode())
#
## Receive Message
#data = s.recv(1024)
#print(data)
#
#print("Closing Connection")