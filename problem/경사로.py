import sys
input = sys.stdin.readline

N, L = map(int, input().split())


grid = []


def higher(land: list, N, L):
    visited = [False for _ in range(N)]
    for i in range(1, N):
        if abs(land[i-1] - land[i]) > 1:
            return False
        # 내려간다면
        elif land[i-1] - land[i] == 1:
            for j in range(L):
                if i+j >= N or land[i] != land[i+j] or visited[i+j]:
                    return False
                if land[i] == land[i+j]:
                    visited[i+j] = True
        # 올라간다면
        elif land[i-1] - land[i] == -1:
            for j in range(L):
                if i-j-1 < 0 or land[i-1] != land[i-j-1] or visited[i-j-1]:
                    return False
                if land[i-1] == land[i-j-1]:
                    visited[i-j-1] = True

    return True


for i in range(N):
    temp = list(map(int, input().split()))
    grid.append(temp)

answer = 0
for i in range(N):
    if higher([grid[i][j] for j in range(N)],N,L):
        answer += 1

for j in range(N):
    if higher([grid[i][j] for i in range(N)],N,L):
        answer += 1

print(answer)
