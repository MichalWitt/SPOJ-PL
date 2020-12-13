def linear(a,b,c):
	if a != 0:
		z = (c-b)/a
		print(f"{z:.2f}") #pokazuje dwa zera po kropce 
	elif a == 0:
		if (c-b) == 0:
			print("NWR")
		else:
			print("BR")

x = list(map(float,input().split()))
a = round(x[0], 2)
b = round(x[1], 2)
c = round(x[2], 2)
linear(a,b,c)
exit()
