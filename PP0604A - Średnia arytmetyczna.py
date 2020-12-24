for i in range(int(input())):
   x = [int(i) for i in input().split()]
   x1 = x[1:]
   av =  float(sum(x1)/(len(x1))) 
   tmp = []
   for i in range(len(x1)):
      k = av-x1[i]
      if k<0:
         k=k*(-1)
      if i == 0:
         tmp.append(x1[i])   
         tmp.append(k)
      elif k < tmp[1]:
         tmp.clear()
         tmp.append(x1[i])   
         tmp.append(k)
      elif k >= tmp[1]:
         continue
   print(tmp[0]) 