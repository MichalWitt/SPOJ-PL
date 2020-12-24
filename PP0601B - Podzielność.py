for i in range(int(input())):
   n,x,y = [int(i) for i in input().split()]
   wynik = [] 
   for i in range(1,n):
      if i % x == 0 and i % y != 0:
         wynik.append(i)
   print(*wynik)
   wynik.clear() 
   
exit() 
   