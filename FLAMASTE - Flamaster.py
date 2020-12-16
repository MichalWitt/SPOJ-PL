t = int(input()) 
for l in range(t):   
   text = input().upper()
   wynik = ''
   last = '' 
   s = int(len(text)) 
   counter = 1
   for i in range(s):
      if s == 1:
         wynik += text[i] 
         continue           
      if text[i] == last:
         counter += 1
         if i == (s-1) and counter >= 3:
            wynik += text[i] + str(counter)                     
         elif i == (s-1) and counter <= 2:
            wynik += text[i]*counter                 
      elif text[i] != last:
         if i == 0:
            last = text[i]
         elif i == (s-1) and counter >= 3: 
            wynik += last + str(counter) + text[i]                         
         elif i == (s-1) and counter <= 2: 
            wynik += last*counter + text[i]                                  
         else:
            if counter >= 3:
               wynik += last + str(counter) 
               counter = 1
               last = text[i]
            else:
               wynik += last*counter
               counter = 1
               last = text[i] 
   print(wynik.rstrip()) 
exit(0)  
   