N, L, R = (int(x) for x in input().split())

A = [x + 1 for x in range(N)]

l_to_r = A[L - 1 : R]
r_to_l = list(reversed(l_to_r))
A_ = A[: L - 1] + r_to_l + A[R:]

print(" ".join(map(str, A_)))
