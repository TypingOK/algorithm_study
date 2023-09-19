import sys
input = sys.stdin.readline

N = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = []
teacher = []
for i in range(N):
    temp = list(input().split())

    for j in range(N):
        if temp[j] == "T":
            teacher.append((i, j))
    graph.append(temp)

answer = False


def dfs(depth):
    global answer
    if depth == 3:
        for i, j in teacher:
            for k in range(4):
                index = 1
                while index <= N:
                    nx = i + dx[k] * index
                    ny = j + dy[k] * index
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] == "S":

                            return False
                        elif graph[nx][ny] == "O":
                            break
                    if 0 > nx and nx > N and 0 > ny and ny > N:
                        break
                    index += 1
        answer = True
        return True

    for i in range(N):
        for j in range(N):
            if graph[i][j] == "X":
                graph[i][j] = "O"
                dfs(depth + 1)
                graph[i][j] = "X"


dfs(0)
if answer == True:
    print("YES")
else:
    print("NO")
