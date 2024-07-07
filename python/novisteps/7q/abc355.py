A, B = (int(x) for x in input().split())

suspects = [1, 2, 3]
suspects.remove(A)
if B in suspects:
    suspects.remove(B)

if len(suspects) == 1:
    print(suspects[0])
else:
    print(-1)
