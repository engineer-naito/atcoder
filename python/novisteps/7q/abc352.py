N, X, Y, Z = (int(x) for x in input().split())

list_ = list(range(X, Y + 1)) if X <= Y else list(range(X, Y - 1, -1))

if Z in list_:
    print("Yes")
else:
    print("No")
