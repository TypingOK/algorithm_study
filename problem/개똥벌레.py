import sys

input = sys.stdin.readline
N, H = map(int, input().split())

lower_t = []
uppwer_t = []

for i in range(N):
    if i % 2 == 0:
        lower_t.append(int(input()))
    else:
        uppwer_t.append(int(input()))
lower_t.sort()
uppwer_t.sort()


answer_count = 0
answer_min_count = sys.maxsize
for i in range(1, H+1):
    count = 0

    left_lower = 0
    right_lower = len(lower_t) - 1
    while (left_lower <= right_lower):
        mid = (left_lower+right_lower) // 2
        if lower_t[mid] <= i-1:
            left_lower = mid + 1
        else:
            right_lower = mid - 1

    count += (len(lower_t) - (right_lower + 1))

    left = 0
    right = len(uppwer_t) - 1
    while (left <= right):
        mid = (left+right) // 2
        if uppwer_t[mid] <= H - i:
            left = mid + 1
        else:
            right = mid - 1
    count += (len(uppwer_t) - (right + 1))

    if count < answer_min_count:
        answer_min_count = count
        answer_count = 1
    elif count == answer_min_count:
        answer_count += 1

print(answer_min_count, answer_count)
