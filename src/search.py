# script for online indexing document and search data in it

import sys
import datrie
import re

filename = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Put filename for indexing")

trie = datrie.Trie.load("../data/odict.trie")

text = []
indexed = {}

with open(filename, 'r') as f:
    text = f.read().split('\n')

for row_i, row in enumerate(text):
    if (len(row) == 0):
        continue
    for lexeme in re.findall(r"[\w']+", row):
        if len(lexeme)==0:
            continue
        lex = lexeme.lower()
        if lex in trie:
            lex = trie[lex].split("=")[0]
        if lex in indexed:
            indexed[lex].append(row_i)
        else:
            indexed[lex] = [row_i]


print(indexed)
