N, K, X = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

B = A[:K] + [X] + A[K:]
print(" ".join(map(str, B)))
