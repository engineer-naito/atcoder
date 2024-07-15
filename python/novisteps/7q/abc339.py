S = input()

result = ""
for s in reversed(S):
    if s == ".":
        break
    result = s + result
print(result)
