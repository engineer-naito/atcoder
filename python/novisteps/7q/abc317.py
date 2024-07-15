N = int(input())
A = [int(x) for x in input().split()]
A.sort()

for i in range(N):
    if i == 0:
        continue
    if A[i - 1] + 1 != A[i]:
        print(A[i - 1] + 1)
        break
