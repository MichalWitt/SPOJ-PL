while True:           
    try:
        a, b, c = input().split(' ')
        dluga = (len(a))
        dlugb = (len(b))
       
        if dluga or dlugb <= 999:         
                       
            if b == '==':
                if a == c:
                    print('1')
                else:
                    print('0')
               
            elif b == '!=':
                if a != c:
                    print('1')
                else:
                    print('0')
               
            elif b == '>=':
                a, c = int(a), int(c)
                
                if a >= c:
                    print('1')
                else:
                    print('0')
                   
            elif b == '<=':
                a, c = int(a), int(c)
                if a <= c:
                    print('1')
                else:
                    print('0')         
    except EOFError:
        break        
