import sys
from collections import deque
sys.setrecursionlimit(15000)
input = sys.stdin.readline


# def dfs(num, N, start, visit):
#     count[start] += 1

#     visit.add(num)
#     for i in computer[num]:
#         if(i not in visit):
#             dfs(i, N, start, visit)

def bfs(start):
    count = 1
    q = deque()
    q.append(start)
    visit[start] = True
    while(q):
        temp = q.popleft()
        for i in computer[temp]:
            if(not visit[i]):
                count+=1
                visit[i] = True
                q.append(i)
    return count

N, M = map(int, input().split())

computer = [[] for i in range(N)]

visit = [False] * N

count = [0]*N

for i in range(M):
    A, B = map(int, input().split())
    computer[B-1].append(A-1)

# print(computer)

for i in range(N):
    count[i] = bfs(i)
    visit = [False] * N
    

maxVal = max(count)
# print(maxVal)

for i in range(len(count)):
    if(count[i] == maxVal):
        print(i+1, end=" ")
