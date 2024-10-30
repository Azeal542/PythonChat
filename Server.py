import socket

while True:
    # Setting up Network settings
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server = "127.0.0.1"
    port = 80
    # Connecting to the server
    server_address = ((server,port))
    s.bind(server_address)
    s.listen(1)
    print("Server is listening on port",port)
    connection, client_address = s.accept()
    print("Connection from",client_address)
    mode = connection.recv(4).decode()
    print(mode)
    try:
        if mode == "POST":    
            check = connection.sendall(b"ACK")
            data = connection.recv(1024).decode()
            print(data)
            if '/kill' in data:
                exit()
            elif data:
                with open("log.txt","a") as log:
                    log.write(str(data)+"\n")
            else:
                print("No data received")
        elif mode == "GET":
            check = connection.sendall(b"ACK")
            with open("log.txt","r") as log:
                data = log.read()
                connection.sendall(data.encode())
        else:
            print("Invalid mode")
    finally:
        connection.close()
        s.close()

connection.sendall(b"Invalid mode")

# Send Message


# Receive Message
#data = s.recv(10)
#print(data)

print("Recieved data")