A, B = (int(x) for x in input().split())

for x in range(9):
    if x != A + B:
        print(x)
        break
