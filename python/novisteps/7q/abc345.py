S = input()

first = S[:1]
last = S[-1:]
if S[:1] == "<" and S[-1:] == ">" and len(list(set(S[1:-1]))) == 1 and S[1:-1][0] == "=":
    print("Yes")
else:
    print("No")
