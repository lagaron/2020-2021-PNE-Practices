import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.124.179"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

# -- Waits for a client to connect
print("Waiting for Clients to connect")
ls.accept()

print("A client has connected to the server!")
count_connections=0

# -- Close the socket
ls.close()
print("The server is configured")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        count_connections +=1
        print("CONNECTION" + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    # -- Read the message from the client
    # -- The received message is in raw bytes
    msg_raw = cs.recv(2048)

    # -- We decode it for converting it
    # -- into a human-redeable string
    msg = msg_raw.decode()

    # -- Print the received message
    print( "Message received: {msg}")

    # -- Send a response message to the client
    try:
        response = int(msg) ** int(msg)

    # -- The message has to be encoded into bytes
    cs.send(str(response).encode())

    # -- Close the data socket
    cs.close()

    if count_connections ==5:
        for i in range(0, len(client_address_list)):
