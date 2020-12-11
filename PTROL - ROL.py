x = []
def intnastr(x): #zamienia inty w liście na stringi
   string_ints = [str(int) for int in x] 
   str_of_ints = " ". join(string_ints) 
   print(str_of_ints)
for i in range(int(input())):   
   x = list(map(int, input().split()))
   del x[0]
   x += [x.pop(0)] #przesuwa element[0] na koniec listy
   intnastr(x)