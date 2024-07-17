N = int(input())
SC_list = [tuple(x for x in input().split()) for _ in range(N)]

T = sum(int(SC[1]) for SC in SC_list)
sorted_SC_list = sorted(SC_list, key=lambda x: x[0])

print(sorted_SC_list[T % N][0])
