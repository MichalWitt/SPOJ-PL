import sys
try:
    liczby = [] 
    for liczba in sys.stdin: 
        liczby.append(int(liczba))
        print(sum(liczby))
except:
    sys.exit(0) 
