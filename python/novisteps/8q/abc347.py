N, K = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

result = [str(int(x / K)) for x in A if x % K == 0]
print(" ".join(result))
