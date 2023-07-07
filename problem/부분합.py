import sys

input = sys.stdin.readline
N, S = map(int, input().split())

numbers = list(map(int, input().split()))

left = 0
right = 0
answer = sys.maxsize
count = numbers[0]

while left <= right:
    # print(count, left, right)
    if count == S:
        answer = min(answer, right - left)
        if right != left:
            count -= numbers[left]
            left += 1
        elif right + 1 < N:
            right += 1
            count += numbers[right]
    elif count < S:
        if right + 1 < N:
            right += 1
            count += numbers[right]
        else:
            break
    else:
        answer = min(answer, right-left)
        count -= numbers[left]
        left += 1
    if answer + 1 == 1:
        break
if answer == sys.maxsize:
    print(0)
else:
    print(answer+1)
