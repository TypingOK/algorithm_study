import sys

input = sys.stdin.readline
N, M = map(int, input().split())

times = []

for i in range(N):
    times.append(int(input()))

times.sort()

left = 1
right = int(1e9 * M)
answer = int(sys.maxsize)

while (left <= right):
    mid = (left+right) // 2
    count = sum((mid//time) for time in times)

    if count >= M:
        answer = min(answer, mid)
        right = mid-1
    else:
        left = mid+1

print(answer)
