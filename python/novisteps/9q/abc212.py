A, B = (int(x) for x in input().split())

if A == B == 0:
    pass
elif B == 0:
    print("Gold")
elif A == 0:
    print("Silver")
else:
    print("Alloy")
