import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    word = deque(input().split())
    answer = ""

    while word:
        c = word.popleft()
        if len(answer) == 0:
            answer = c
        else:
            if answer[0] >= c:
                answer = c + answer
            else:
                answer += c
    print(answer)
