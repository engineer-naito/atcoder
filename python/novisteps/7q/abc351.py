N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

found = False
for i, a in enumerate(A):
    for j, x in enumerate(a):
        if x != B[i][j]:
            found = True
            print(f"{i + 1} {j + 1}")
            break
    if found:
        break
