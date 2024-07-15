N, L = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

passed_count = 0
for i in range(N):
    if A[i] >= L:
        passed_count += 1
print(passed_count)
