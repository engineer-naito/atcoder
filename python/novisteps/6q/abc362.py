xA, yA = (int(x) for x in input().split())
xB, yB = (int(x) for x in input().split())
xC, yC = (int(x) for x in input().split())

AB_squared = (xA - xB) ** 2 + (yA - yB) ** 2
BC_squared = (xB - xC) ** 2 + (yB - yC) ** 2
CA_squared = (xC - xA) ** 2 + (yC - yA) ** 2

lens = [AB_squared, BC_squared, CA_squared]
lens.sort()

if lens[0] + lens[1] == lens[2]:
    print("Yes")
else:
    print("No")
