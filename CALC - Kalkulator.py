while True:            
    try:               
        a,b,c = input().split(' ')
        a,b,c = str(a),int(b),int(c)
        if a == '+':
            print(b+c)
        elif a == '-':
            print(b-c)
        elif a == '*':
            print(b*c)
        elif a =='/':
            if c == '0':
                continue
            else:
                print(int(b/c))
        elif a == '%':
            print(b%c)
    except EOFError:
        break
