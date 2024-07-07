S = input()

times = int(S[3:])
if times < 350:
    if times in {0, 316}:
        print("No")
    else:
        print("Yes")
else:
    print("No")
