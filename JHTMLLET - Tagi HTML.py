import sys
htm = sys.stdin.read()
newtxt = '' 
z = True
size = int(len(htm)) 
for i in range(size):
   if htm[i] == "<":
      z = True
   elif htm [i] == ">":
      z = False
   if z == True:
      newtxt += htm[i].upper()
   if z == False:
     newtxt += htm[i]      
   
print(newtxt) 
exit() 