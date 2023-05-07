import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

answer = 0

words = []
for i in range(N):
    words.append(input().rstrip('\n'))

words.sort(key=len)
for i in range(N):
    flag = False
    for j in range(i+1, N):
        if words[i] == words[j][:len(words[i])]:
            flag = True
            break
    if not flag:
        answer += 1
print(answer)
