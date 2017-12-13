# this script print to stdout lemmatization of test file

import datrie
import re
import sys

test_name = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Put test filename")

trie = datrie.Trie.load("../data/odict.trie")

with open(test_name, 'r') as f:
    text = f.read().split('\n')
    for row in text:
        if len(row) == 0:
            continue
        for lexeme in re.findall(r"[\w']+", row):
            if len(lexeme) == 0:
                continue
            if lexeme.lower() in trie:
                print(lexeme + "{" + trie[lexeme.lower()] + "}", end=' ')
            else:
                print(lexeme + "{" + lexeme + "=S}", end=' ')
        print()
