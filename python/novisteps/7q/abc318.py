N, M, P = (int(x) for x in input().split())

count = 0
for i in range(2 * 10**5 + 1):
    if M + i * P <= N:
        count += 1
        continue
    break
print(count)
