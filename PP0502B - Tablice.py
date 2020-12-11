t  = int(input())
for i in range(t):
   rev = list(map(int,input().split()))
   ile = rev[0] + 1
   if len(rev) == ile:
      x = rev[::-1]
      x.pop()        #usunięcie ostatniego elementu
      string_ints = [str(int) for int in x] 
      str_of_ints = " ". join(string_ints) 
      print(str_of_ints)
   else:
      continue
exit()
