import datrie
import re

trie = datrie.Trie.load("odict.trie")

with open('test.txt', 'r') as f:
    text = f.read().split('\n')
    for row in text:
        if (len(row) == 0):
            continue
        for lexeme in re.findall(r"[\w']+", row):
            if len(lexeme)==0:
                continue
            if lexeme.lower() in trie:
                print(lexeme + "{" + trie[lexeme.lower()] + "}", end=' ')
            else:
                print(lexeme +"{" + lexeme + "=S}", end=' ')
        print()


