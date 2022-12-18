import sys
input = sys.stdin.readline

N = int(input())
visit = [False] * N
numbers = []
for i in range(N):
    numbers.append(list(map(int, input().split())))
answer = int(1e9)


def dfs(depth, index):
    global answer
    if(depth == N//2):
        count_start, count_link = 0, 0
        for x in range(N):
            for y in range(N):
                if(visit[y] and visit[x]):
                    count_start += numbers[x][y]
                elif(not visit[x] and not visit[y]):
                    count_link += numbers[x][y]
        answer = min(abs(count_start-count_link), answer)
        return
    for i in range(index, N):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i+1)
            visit[i] = False


dfs(0, 0)
print(answer)
