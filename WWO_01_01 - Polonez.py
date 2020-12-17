import sys
a, b, c = [int(i) for i in input().split()]
names = sys.stdin.read().split()
girls = []
boys = [] 
for name in names:
   if name[-1] == "a":
      girls.append(name)
   else:
      boys.append(name)
if len(boys) >= len(girls):
   print(len(girls))
else:
   print(len(boys))
exit() 



   
