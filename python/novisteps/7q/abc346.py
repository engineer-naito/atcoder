N = int(input())
A = [int(x) for x in input().split()]

B = []
for i, a in enumerate(A):
    if i != len(A) - 1:
        B.append(a * A[i + 1])
print(" ".join(map(str, B)))
