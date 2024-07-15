A, B, D = (int(x) for x in input().split())

nums = [A]
while True:
    next_num = nums[-1] + D
    if next_num > B:
        break
    nums.append(next_num)
    if next_num == B:
        break

print(" ".join(map(str, nums)))
