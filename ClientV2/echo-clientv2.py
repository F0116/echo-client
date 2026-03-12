# echo-client.py
import socket
HOST = "10.90.14.70" # The server's hostname or IP address
PORT = 65432 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    while True:
        msg = input("You: ")

        s.sendall(msg.encode())

        if msg.lower() == "exit":
            print("Connection lost")
            break
    
        data = s.recv(1024)
        print(f"Server: {data.decode()}")