N, X = (int(i) for i in input().split())
S = [int(x) for x in input().split()]

total = 0
for s in S:
    if s <= X:
        total += s
print(total)
