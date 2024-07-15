N = int(input())

result = ""
for x in range(N):
    if (x + 1) % 3 == 0:
        result += "x"
    else:
        result += "o"
print(result)
