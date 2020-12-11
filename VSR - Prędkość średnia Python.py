def srednia(v1, v2):
   x = 2 * v1 * v2 / (v1+v2)
   print(int(x)) 

for i in range(int(input())):
   v1, v2 = map(int,input().split())
   srednia(v1, v2)

exit() 