from collections import deque
import sys

input = sys.stdin.readline

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())


def BFS(start, end, chess_map, I):
    q = deque()
    q.append([start[0], start[1]])
    visited = [[False for _ in range(I)] for _ in range(I)]
    count = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            if x == end[0] and y == end[1]:
                return count

            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
        count += 1
    return count


for i in range(T):
    I = int(input())
    chess_map = [[0 for _ in range(I)] for _ in range(I)]

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    min_result = BFS(start, end, chess_map, I)
    print(min_result)
