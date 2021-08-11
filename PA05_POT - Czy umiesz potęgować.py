import sys
input()
while True:
   try:
      
      a,b=input().split(' ')
      if a[-1] == '0' or a[-1]=='1' or a[-1]=='5' or a[-1]=='6':
         wynik = a[-1]
         wynik = int(wynik)
         print(wynik) 

      elif a[-1] == '2':
         b=int(b) 
         if b%4==0: print(6)
         elif b%4==3: print(8)
         elif b%4==2: print(4)
         elif b%4==1: print(2)
      elif a[-1] == '3':
         b=int(b) 
         if b%4==0: print(1)
         elif b%4==3: print(7)
         elif b%4==2: print(9)
         elif b%4==1: print(3)      
      elif a[-1] == '7':
         b=int(b) 
         if b%4==0: print(1)
         elif b%4==3: print(3)
         elif b%4==2: print(9)
         elif b%4==1: print(7)
      elif a[-1] == '8':
         b=int(b) 
         if b%4==0: print(6)
         elif b%4==3: print(2)
         elif b%4==2: print(4)
         elif b%4==1: print(8)
      elif a[-1] == '4':
         b=int(b) 
         if b%2==0: print(6)
         if b%2!=0: print(4)
      elif a[-1] == '9':
         b=int(b) 
         if b%2==0: print(1)
         if b%2!=0: print(9)  
      
   except:
      sys.exit(0)

   

