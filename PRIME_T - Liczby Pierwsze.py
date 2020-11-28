#  


while True:
    try:
        for a in range(1, 10000):#pierwsza petla wykona sie 10 000 razy, (tyle liczb zostanie zprawdzonych czy sa pierwsze)
            n = int(input())
            if n > 10000 or n < 1: 
                continue
            for x in range(2, int(n ** 0.5) + 1, +1):#druga petla w zakresie od 2 do pierwiastka z wprowadzonej liczby n +1
                if n % x == 0: #jeżeli wprowadzona liczba ma jakies dzielniki w zakresie od 2 do pierwiastka z n +1
                    print('NIE')
                    break
            else:
                if n == 1:
                    print('NIE')
                else:
                    print('TAK')
    except EOFError:
        break



        
