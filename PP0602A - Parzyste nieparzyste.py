for i in range(int(input())):
   dane = [int(i) for i in input().split()]
   size = int(len(dane))
   x = []
   [x.append(dane[i]) for i in range(2,size,2)]
   [x.append(dane[i]) for i in range(1,size,2)]
   print(*x)
   x.clear()
      