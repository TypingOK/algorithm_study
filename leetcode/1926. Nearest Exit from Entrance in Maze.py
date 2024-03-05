# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque


class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        q.append((entrance[0], entrance[1]))
        visited = [[False for _ in range(len(maze[0]))]
                   for _ in range(len(maze))]
        visited[entrance[0]][entrance[1]] = True

        N = len(maze)
        M = len(maze[0])
        count = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.popleft()

                if not (x == entrance[0] and y == entrance[1]) and (x == 0 or y == 0 or x == N-1 or y == M-1):
                    return count

                for i in range(4):
                    nx = x + self.dx[i]
                    ny = y + self.dy[i]

                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == '.':
                        q.append((nx, ny))
                        visited[nx][ny] = True
            count += 1

        return -1
