import sys
import socket

host = "127.0.0.1"
port = 5555

filename = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Put filename for indexing")

with open(filename, 'r') as f:
    text = f.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("[+] Connected to bind shell!\n")
s.send(text.encode("utf-8"))
result = s.recv(1024).decode('utf-8')
print(result)