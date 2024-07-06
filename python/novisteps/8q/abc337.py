N = int(input())

scores = [[int(x) for x in input().split()] for _ in range(1, N + 1)]

takahashi = 0
aoki = 0
for score in scores:
    takahashi += score[0]
    aoki += score[1]

if takahashi < aoki:
    print("Aoki")
elif takahashi == aoki:
    print("Draw")
else:
    print("Takahashi")
