import sys
input()
while True:

   try:
      
      klasa,cuk=input().split(' ')
      klasa, cuk = int(klasa), int(cuk)
      klasa = klasa-1
      if klasa == 0: print("TAK") #JAŚ SAM W KLASIE
      elif cuk>klasa and cuk%klasa != 0: print("TAK")#WIECEJ CUKIERKÓW, NIE DA SIĘ PODZIELIĆ PO RÓWNO
      elif cuk<klasa: print("TAK") #ZA MAŁO CUKIERKÓW DLA WSZYSTKICH
      elif cuk == klasa: print("NIE") #TYLE OSÓB ILE CUKIERKÓW
      elif cuk>klasa and cuk%klasa == 0: print("NIE")#WIECEJ CUKIERKOW, DA SIĘ PODZIELIĆ PO RÓWNO
      
   except:
      sys.exit(0)

   

