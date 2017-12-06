# this script make trie from odict.csv

import codecs
import datrie
import csv 

russian = 'абвгдеёжзиклмнопрстуфхцчъыьэюя'
trie = datrie.Trie(russian)

# pr: part of speech
pr = {}
pr['св-нсв'] = 'V'
pr['ж'] = 'S'
pr['п'] = 'A'
pr['числ.'] = 'ADV'
pr['предл.'] = 'PR'
pr['н'] = 'ADV'
pr['предик.'] = 'ADV'
pr['част.'] = 'ADV'
pr['мс-п'] = 'ADV'
pr['межд.'] = 'ADV'
pr['мн.']  = 'S'
pr['мо-жо'] = 'S'
pr['союз'] = 'CONJ'
pr['сравн.'] = 'ADV'
pr['числ.-п'] = 'ADV'
pr['мо'] = 'S'
pr['м'] = 'S'
pr['вводн.'] = 'ADV'
pr['нсв'] = 'V'
pr['св'] = 'V'
pr['со'] = 'S'
pr['жо'] = 'S'
pr['с'] = 'S'

# make trie from odict dataset
with codecs.open('../data/odict.csv', "r", 'cp1251') as lexemes:
    reader = csv.reader(lexemes, delimiter=',')
    for row in reader:
        for i in range(len(row)): 
            # skip empty and delimeter element
            if i != 1 and row[i] != '': 
                # trie value form like: infinitive=ADV
                trie[row[i]] = row[0] + "=" + pr[row[1]]

trie.save("../data/odict.trie")
