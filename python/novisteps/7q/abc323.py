S = input()

is_zero_list = []
for i, s in enumerate(S):
    if i % 2:
        is_zero_list.append(s == "0")

print("Yes" if all(is_zero_list) else "No")
