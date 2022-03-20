z = int(input())
while True:
	try:
		a, b = [int(i) for i in input().split()]
		c = 0
		x = a*b
		if a < b: 
			c += b
		else:
			c +=a
		while c <= x:
			if c%a==0 and c%b==0:
				print(c)
				break
			c+=1
	except EOFError:
		break