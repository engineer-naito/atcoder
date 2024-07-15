N = int(input())
S = input()

if "ABC" not in S:
    print(-1)
    pass

for i, s in enumerate(S):
    if i <= N - 3 and s == "A" and S[i + 1] == "B" and S[i + 2] == "C":
        print(i + 1)
        break
