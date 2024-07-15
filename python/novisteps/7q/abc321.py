N = input()

previous = int(N[0])
is_like_321 = True
for i, n in enumerate(N):
    if i == 0:
        continue
    previous = int(N[i - 1])
    if previous <= int(n):
        is_like_321 = False
        break
print("Yes" if is_like_321 else "No")
