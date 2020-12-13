while True:            
	try:               
		def half(x):
			new = ''
			pol = int(len(x)/2)
			for i in range(0, pol):
				new += x[i]
			print(new)
		x = []
		for i in range(int(input())):
			x = input()
			if len(x) % 2 == 0:
				half(x)
			else:
				continue
	except EOFError:
		break