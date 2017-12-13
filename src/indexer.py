import sys
import socket
import json

host = "127.0.0.1"
port = 5555

filename = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Put filename for indexing")

with open(filename, 'r') as f:
    text = f.read()

# get current index
with open("index.data", 'r') as f2:
    index = json.load(f2)

print(index)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(text.encode("utf-8"))
result = s.recv(1024).decode('utf-8')
result = json.loads(result)
for key in result:
    if key in index:
        if filename in index[key]:
            break
            # if file already indexed

        index[key][filename] = result[key]
    else:
        index[key] = {filename: result[key]}

with open("index.data", 'w') as f3:
    json.dump(index, f3, ensure_ascii=False)
