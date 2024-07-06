N = int(input())

result = ""
for i in range(2 * N + 1):
    if i % 2 == 0:
        result += "1"
    else:
        result += "0"
print(result)
