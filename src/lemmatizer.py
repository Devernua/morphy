# script for online indexing document and search data in it

import datrie
import re
import socket
import json

trie = datrie.Trie.load("../data/odict.trie")
print("trie loaded")


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 5555))
    connection.listen(10)
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(2048).decode("utf-8")
            print("data: \n", data)
            indexed = {}
            for row_i, row in enumerate(data.split("\n")):
                if len(row) == 0:
                    continue
                for l_i, lexeme in enumerate(re.findall(r"[\w']+", row)):
                    if len(lexeme) == 0:
                        continue
                    lex = lexeme.lower()
                    if lex in trie:
                        lex = trie[lex].split("=")[0]
                    if lex in indexed:
                        indexed[lex].append([row_i, l_i])
                    else:
                        indexed[lex] = [[row_i, l_i]]

            current_connection.send(json.dumps(indexed).encode("utf-8"))
            current_connection.close()
            break


listen()
