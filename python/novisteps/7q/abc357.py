S = input()

upper_count = 0
lower_count = 0

for s in S:
    if s.isupper():
        upper_count += 1
    elif s.islower():
        lower_count += 1

if upper_count > lower_count:
    print(S.upper())
else:
    print(S.lower())
