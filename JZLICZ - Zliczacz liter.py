import sys
dict = {}
ile = int(input())
for wiersz in sys.stdin:
	for litera in wiersz:
		if litera not in dict and litera != "\n" and litera != " ":
			dict.update({litera: 1})
		elif litera in dict and litera != "\n" and litera != " ":
			dict[litera] += 1   


#WZORZEC
klucze = sorted(list(dict))
klucze1 = ''.join(klucze)
while klucze1[0].istitle():
	klucze1 = klucze1[1:]+klucze1[0]

#******
dict1={} 
for i in klucze1:
	dict1.update({i: dict[i]})
for klucz in dict1:
    print(klucz, dict1[klucz])	