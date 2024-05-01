import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

RStart = [0, 0]
BStart = [0, 0]
end = [0, 0]
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == "R":
            RStart[0] = i
            RStart[1] = j
            temp[j] = "."
        elif temp[j] == "B":
            BStart[0] = i
            BStart[1] = j
            temp[j] = "."
        elif temp[j] == "O":
            end[0] = i
            end[1] = j

    graph.append(temp[:-1])

index = 0
# visited = [[False for _ in range(M)] for _ in range(N)]
q = deque()
q.append((RStart+BStart, 1))
while index < 10 and q:
    index += 1
    size = len(q)
    for _ in range(size):
        temp, count = q.popleft()
        # print(temp, count)
        rb = temp[:2]
        bb = temp[2:]
        r = deepcopy(rb)
        b = deepcopy(bb)
        # 위로 올리기
        # 누가 더 위에 있는지 확인, 만약 B가 더 높게 있다면 B를 먼저 굴려야 함
        if r[0] > b[0]:
            failFlag = False
            for i in range(b[0]-1, -1, -1):
                if graph[i][b[1]] == "#":
                    b[0] = i+1
                    break
                elif graph[i][b[1]] == "O":
                    failFlag = True
                    break
            for i in range(r[0]-1, -1, -1):
                if graph[i][r[1]] == "#":
                    r[0] = i+1
                    break
                elif graph[i][r[1]] == "O":
                    if failFlag:
                        break
                    else:
                        print(count)
                        exit()
            if r == b:
                r[0] += 1
            if not failFlag and (b[0] != bb[0] or r[0] != rb[0]):
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))
        elif r[0] <= b[0]:
            successFlag = False
            failFlag = False
            for i in range(r[0]-1, -1, -1):
                if graph[i][r[1]] == "#":
                    r[0] = i+1
                    break
                elif graph[i][r[1]] == "O":
                    successFlag = True
                    break
            for i in range(b[0]-1, -1, -1):
                if graph[i][b[1]] == "#":
                    b[0] = i+1
                    break
                elif graph[i][b[1]] == "O":
                    failFlag = True
                    break
            if successFlag and not failFlag:
                print(count)
                exit()
            if r == b:
                b[0] += 1
            if (b[0] != bb[0] or r[0] != rb[0]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        # 아래로 내리기
        r = deepcopy(rb)
        b = deepcopy(bb)
        if r[0] < b[0]:

            failFlag = False
            for i in range(b[0]+1, N):
                if graph[i][b[1]] == "#":
                    b[0] = i-1
                    break
                elif graph[i][b[1]] == "O":
                    failFlag = True
                    break
            for i in range(r[0]+1, N):
                if graph[i][r[1]] == "#":
                    r[0] = i-1
                    break
                elif graph[i][r[1]] == "O":
                    if failFlag:
                        break
                    else:
                        print(count)
                        exit()
            if r == b:
                r[0] -= 1
            if (b[0] != bb[0] or r[0] != rb[0]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        elif r[0] >= b[0]:
            successFlag = False
            failFlag = False
            for i in range(r[0]+1, N):
                if graph[i][r[1]] == "#":
                    r[0] = i-1
                    break
                elif graph[i][r[1]] == "O":
                    successFlag = True
                    break
            for i in range(b[0]+1, N):
                if graph[i][b[1]] == "#":
                    b[0] = i-1
                    break
                elif graph[i][b[1]] == "O":
                    failFlag = True
                    break
            if successFlag and not failFlag:
                print(count)
                exit()
            if r == b:
                b[0] -= 1

            if (b[0] != bb[0] or r[0] != rb[0]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        # 왼쪽으로 기울이기
        # 작은 수라면 좀 더 왼쪽에 있기 때문에 먼저 굴려야 한다
        r = deepcopy(rb)
        b = deepcopy(bb)

        if r[1] > b[1]:
            failFlag = False
            for i in range(b[1]-1, -1, -1):
                if graph[b[0]][i] == "#":
                    b[1] = i+1
                    break
                elif graph[b[0]][i] == "O":
                    failFlag = True
                    break
            for i in range(r[1]-1, -1, -1):
                if graph[r[0]][i] == "#":
                    r[1] = i+1
                    break
                elif graph[r[0]][i] == "O":
                    if failFlag:
                        break
                    else:
                        print(count)
                        exit()
            if r == b:
                r[1] += 1
            if (b[1] != bb[1] or r[1] != rb[1]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        elif r[1] <= b[1]:
            successFlag = False
            failFlag = False
            for i in range(r[1]-1, -1, -1):
                if graph[r[0]][i] == "#":
                    r[1] = i+1
                    break
                elif graph[r[0]][i] == "O":
                    successFlag = True
                    break
            for i in range(b[1]-1, -1, -1):
                if graph[b[0]][i] == "#":
                    b[1] = i+1
                    break
                elif graph[b[0]][i] == "O":
                    failFlag = True
                    break
            if successFlag and not failFlag:
                print(count)
                exit()
            if r == b:
                b[1] += 1
            if (b[1] != bb[1] or r[1] != rb[1]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        # 오른쪽으로 기울이기
        # 더 크다면 오른쪽에 있기 때문에 큰 녀석 먼저
        r = deepcopy(rb)
        b = deepcopy(bb)
        if r[1] < b[1]:
            failFlag = False
            for i in range(b[1]+1, M):
                if graph[b[0]][i] == "#":
                    b[1] = i-1
                    break
                elif graph[b[0]][i] == "O":
                    failFlag = True
                    break
            for i in range(r[1]+1, M):
                # print(graph[r[0]][i])
                if graph[r[0]][i] == "#":
                    r[1] = i-1
                    break
                elif graph[r[0]][i] == "O":
                    if failFlag:
                        break
                    else:
                        print(count)
                        exit()
            if r == b:
                r[1] -= 1
            if (b[1] != bb[1] or r[1] != rb[1]) and not failFlag:
                # print(r, b, count)
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

        elif r[1] >= b[1]:
            successFlag = False
            failFlag = False
            for i in range(r[1]+1, M):
                if graph[r[0]][i] == "#":
                    r[1] = i-1
                    break
                elif graph[r[0]][i] == "O":
                    successFlag = True
                    break
            for i in range(b[1]+1, M):
                if graph[b[0]][i] == "#":
                    b[1] = i-1
                    break
                elif graph[b[0]][i] == "O":
                    failFlag = True
                    break
            if successFlag and not failFlag:
                print(count)
                exit()
            if r == b:
                b[1] -= 1
            if (b[1] != bb[1] or r[1] != rb[1]) and not failFlag:
                # visited[r[0]][r[1]] = True
                q.append((r+b, count+1))

print(-1)
