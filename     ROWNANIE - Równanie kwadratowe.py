import sys
while True:
    try:
        delta = 0
        def delta(a,b,c):
            d = (b*b)-4*a*c
            if d < 0:
                print("0")
            if d == 0:
                print("1")
            if d > 0:
                print("2")

        x = list(map(float,input().split()))
        a = x[0] 
        b = x[1] 
        c = x[2]

        delta(a,b,c)

    except:
        sys.exit(0) 
