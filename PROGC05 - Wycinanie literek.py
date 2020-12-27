while True:            
   try: 
      a,b = input().split()
      c =''
      for i in b:
        if i != a:
           c += i
      print(c) 
                    
   except EOFError:
      break