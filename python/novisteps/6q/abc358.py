N, A = (int(x) for x in input().split())
T = [int(x) for x in input().split()]

previous_time = 0
for i in range(N):
    time_ = max(previous_time, T[i]) + A
    print(time_)
    previous_time = time_
