while True:            
    try:
        counter = 0
        x = [int(i) for i in input().split()]
        size = len(x) 
        for i in range(2, size):
           if x[i] == x[0]:
              counter += 1
        print(counter) 
              
    except EOFError:
        break