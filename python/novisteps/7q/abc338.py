S = input()

print("Yes" if S[0].isupper() and all(_.islower() for _ in S[1:]) else "No")
