import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001
visited[N] = 0

answer_number = 0
answer_count = 0


q = deque()
q.append(N)

while q:
    x = q.popleft()
    count = visited[x]
    if (x == K):
        answer_number = count
        answer_count += 1
    else:
        for i in (x-1, x+1, x * 2):
            if 0 <= i < 100001 and (visited[i] == 0 or visited[x]+1 == visited[i]):
                q.append(i)
                visited[i] = count+1


print(answer_number)
print(answer_count)
