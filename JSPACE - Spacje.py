import sys
try:

   sms = '' 
   wielka = False
   for wiersz in sys.stdin: 
      for znak in wiersz:
         if znak == ' ':
            wielka = True
         elif znak != ' ':
            if (wielka):
               sms += znak.upper()
               wielka = False
            else:
               sms += znak
   print(sms)

except:
   sys.exit(0)          
         
         
      