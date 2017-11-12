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

with codecs.open('odict.csv', "r", 'cp1251') as lexemes:
    reader = csv.reader(lexemes, delimiter=',')
    for row in reader:
        for i in range(len(row)): 
            if i != 1 and row[i] != '':
                trie[row[i]] = row[0] + "=" + pr[row[1]]
        
fin = "авторитаризме"
print(fin + "{" + trie[fin] + "}")
