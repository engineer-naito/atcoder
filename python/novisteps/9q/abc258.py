K = int(input())

if K < 10:
    print(f"21:0{K}")
elif K < 60:
    print(f"21:{K}")
elif K < 70:
    print(f"22:0{K - 60}")
else:
    print(f"22:{K - 60}")
