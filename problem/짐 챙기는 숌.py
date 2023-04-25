import sys

input = sys.stdin.readline
N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    answer = 0
    books = list(map(int, input().split()))

    count = 0
    for i in books:
        if count + i > M:
            answer += 1
            count = i
        elif count + i == M:
            answer += 1
            count = 0
        else:
            count += i
    if count > 0:
        answer += 1
    print(answer)
