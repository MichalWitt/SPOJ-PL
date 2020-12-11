import sys
while True:
   try:
      x = str(input().lower())
      print(x[::-1])       
   except EOFError:
      break