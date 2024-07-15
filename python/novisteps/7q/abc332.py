N, S, K = (int(x) for x in input().split())

P_Q = [(int(x) for x in input().split()) for _ in range(N)]
sum_ = sum(p * q for p, q in P_Q)

print(sum_ if sum_ >= S else sum_ + K)
