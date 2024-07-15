X, Y = (int(x) for x in input().split())

if 0 <= Y - X < 3 or -4 < Y - X < 0:
    print("Yes")
else:
    print("No")
