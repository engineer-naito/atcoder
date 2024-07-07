N = int(input())
H = [int(x) for x in input().split()]

index_ = -1
for index, h in enumerate(H, start=1):
    if h > H[0]:
        index_ = index
        break
print(index_)
