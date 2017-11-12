import codecs

f = codecs.open('odict.csv', "r", 'cp1251')
odict = f.read().split("\r\n")
odict = [[i.split(",")] for i in odict if len(i.split(",")) >= 1 ]

# odict: [[lexeme, tag, slovofoms...]...]

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
pr['c'] = 'S'

f.close()
