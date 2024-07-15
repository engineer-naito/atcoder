N = int(input())
A = [int(x) for x in input().split()]

print("Yes" if len(list(set(A))) == 1 else "No")
