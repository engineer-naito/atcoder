N, M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
X = [[int(x) for x in input().split()] for _ in range(N)]

actual_nutritions = [0] * M
for x in X:
    for i, x_ in enumerate(x):
        actual_nutritions[i] += x_

print("Yes" if all(A[i] <= actual_nutritions[i] for i in range(M)) else "No")
