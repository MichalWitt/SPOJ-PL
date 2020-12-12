import sys
def nwd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    print(a)
 
t  = int(input())
for i in range(t):
   rev = list(map(int,input().split()))
   a = rev[0]
   b = rev[1] 
   rev.clear() 
   nwd(a, b)
exit() 
