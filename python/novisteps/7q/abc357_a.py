N, M = (int(x) for x in input().split())
H = [int(x) for x in input().split()]

sum_ = 0
is_printed = False
for index, h in enumerate(H):
    sum_ += h
    if sum_ <= M:
        continue
    print(index)
    is_printed = True
    break
if not is_printed:
    print(len(H))
