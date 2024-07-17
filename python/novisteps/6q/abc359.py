N = int(input())
A = [int(x) for x in input().split()]

count = 0
for color_num in range(1, N + 1):
    color_num_indexes = [i for i in range(2 * N) if A[i] == color_num]
    if color_num_indexes[0] + 2 == color_num_indexes[1]:
        count += 1
print(count)
