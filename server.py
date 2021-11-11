import socket
import time

IP = "127.0.0.1"
PORT = 5050
ADDR = (IP, PORT)
BUFFER = 5120
DELAY = 0.01

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()

print("Waiting for a connection........")
conn, addr = server.accept()


def send(msg):
	msg = msg.encode()
	msg_len = len(msg)
	send_len = str(msg_len).encode()
	send_len += b' ' * (BUFFER - len(send_len))

	time.sleep(DELAY)
	conn.send(send_len)
	conn.send(msg)

def recv():
	length = conn.recv(BUFFER).decode()
	if length:
		cmd = conn.recv(int(float(length))).decode()
		return cmd

while True:
	path = recv()
	cmd = input(f"{addr[0]}@{path}$ ")
	
	if cmd == "":
		cmd = " "
	
	send(cmd)

	output = recv()
	print(output)

