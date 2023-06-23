import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 10001
answer = sys.maxsize

while (left <= right):
    mid = (left+right) // 2
    count = 0
    index = 1
    s = 0

    while s+index <= N:
        if max(numbers[s:s+index]) - min(numbers[s:s+index]) <= mid:
            index += 1
        else:
            s += index-1
            count += 1
            index = 1

    if count >= M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)
