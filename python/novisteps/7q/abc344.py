A = []
while True:
    input_ = int(input())
    A.append(input_)
    if input_ == 0:
        break

for r in list(reversed(A)):
    print(r)
