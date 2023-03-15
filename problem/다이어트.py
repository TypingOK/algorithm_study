import sys

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
cook = []

line = list(map(int, input().split()))
for i in range(N):
    cook.append(list(map(int, input().split())))
answer = INF
select_food = []
visited = [False] * N


def dfs(depth, cost, visited, select, food):
    global answer
    global select_food
    flag = False
    if (answer < cost):
        return
    for i in range(4):
        if line[i] > select[i]:
            flag = True
            break
    if flag:
        for i in range(depth, N):
            for j in range(4):
                select[j] += cook[i][j]
            food.append(i+1)
            dfs(i+1, cost+cook[i][4], visited, select, food)
            for j in range(4):
                select[j] -= cook[i][j]
            food.pop()
    else:
        if (answer > cost):
            answer = cost
            select_food = food[:]
        return


dfs(0, 0, visited, [0, 0, 0, 0], [])

if (answer == INF):
    print(-1)
else:
    print(answer)
    print(" ".join(map(str, select_food)))
