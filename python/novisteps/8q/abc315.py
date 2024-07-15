S = input()

result = ""
for s in S:
    if s not in ("a", "e", "i", "o", "u"):
        result += s
print(result)
