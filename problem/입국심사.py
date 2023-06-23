import sys

input = sys.stdin.readline
N, M = map(int, input().split())
check = [int(input()) for _ in range(N)]

check.sort()

time_min = 1
time_max = check[-1] * M
answer = 1e9

while (time_min <= time_max):
    mid = (time_min + time_max) // 2
    count = sum(mid//time for time in check)

    if count >= M:
        answer = min(answer, mid)
        time_max = mid-1
    else:
        time_min = mid+1
print(answer)
