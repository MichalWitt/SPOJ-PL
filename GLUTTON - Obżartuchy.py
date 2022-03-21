import math
zestawy = int(input())
while True:
	try:
		guests, cookiesinboxes = [int(i) for i in input().split()]
		day = 86400
		table = []
		def oblicz(x):
			a = int(day/x)
			table.append(a)
		for i in range(guests):
		    oblicz(int(input()))
		print(math.ceil((sum(table))/cookiesinboxes))
	except EOFError:
		break

    