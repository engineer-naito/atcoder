M, D = (int(x) for x in input().split())
y, m, d = (int(x) for x in input().split())

next_y = y
next_m = m
next_d = d + 1
if next_d > D:
    next_m += 1
    next_d = 1
if next_m > M:
    next_m = 1
    next_y += 1

print(next_y, next_m, next_d)
