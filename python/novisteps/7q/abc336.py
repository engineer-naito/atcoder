N = int(input())
bin_N = bin(N)

count = 0
for digit in reversed(bin_N):
    if digit == "1":
        break
    else:
        count += 1
print(count)
