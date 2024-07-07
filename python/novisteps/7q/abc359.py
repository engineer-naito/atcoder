N = int(input())
S = [input() for _ in range(N)]

count = 0
for s in S:
    if s == "Takahashi":
        count += 1
print(count)
