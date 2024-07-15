S = input()

m = 0
r = 0
for index, s in enumerate(S):
    if s == "M":
        m = index
    if s == "R":
        r = index

if m > r:
    print("Yes")
else:
    print("No")
