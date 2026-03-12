import socket

HOST = "10.90.14.67"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            message = data.decode()
            print(f"Client: {message}")

            if message.lower() == "exit":
                print("Client closed the connection")
                break

            conn.sendall(f"Echo: {message}".encode())