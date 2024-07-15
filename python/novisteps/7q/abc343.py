N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

A_ = []
for a in A:
    a_ = []
    for i, _ in enumerate(a):
        if _ == 1:
            a_.append(i + 1)
    A_.append(a_)

for a_ in A_:
    print(" ".join(map(str, a_)))
