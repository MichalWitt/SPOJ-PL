value = int(input())
x = [] 
if value >= 3:
   for i in range(1,value+1,2):
      x.append(i)
   for i in range(0,value+1,2):
      x.append(i)   
   print(*x)
elif value == 0:
   print(value)
else:
   print('NIE')
exit() 

      