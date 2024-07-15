N = int(input())
S = input()

A_flag = False
B_flag = False
C_flag = False
for i, s in enumerate(S):
    if s == "A":
        A_flag = True
    if s == "B":
        B_flag = True
    if s == "C":
        C_flag = True
    if A_flag and B_flag and C_flag:
        print(i + 1)
        break
