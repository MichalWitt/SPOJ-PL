stos = []
licznik = 0
while True:            
    try:
        licznik += 1
        if licznik >= 23:
            break         
        else:
            x = input()
            if x == ('+'):            
                if len(stos) <= 9:                
                    liczba = input()
                    stos.append(liczba)
                    print(':)')                
                elif len(stos) >= 10:
                    liczba = input()
                    print(':(')                                
            elif x == ('-'):                       
                if len(stos) == 0:
                    print(':(')
                else:
                    print(stos.pop())
    except EOFError:
        break
                
                    
            
        
            

