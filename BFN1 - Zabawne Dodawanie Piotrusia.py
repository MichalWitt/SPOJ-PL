z = int(input())
while True:
	try:
		def mirror(x):
		    return x[::-1]
		def ifpali(x, y):
		    if x == y:
		       return True
		    else:
		       return False
		def suma(x, y):
		    a = int(x)+int(y)
		    return str(a) 
		   
		liczba = input()
		rev = mirror(liczba)
		check = ifpali(liczba,rev)
		licznik = 0
		
		if check:
		    print(liczba,  licznik)
		    
		else:
		    while check == False:
		       licznik += 1
		       s = suma(liczba, rev)
		       liczba = s
		       rev = mirror(liczba)
		       check = ifpali(liczba,rev)
		    print(liczba, licznik)
	except EOFError:
		break
    	