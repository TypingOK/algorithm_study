import sys

input = sys.stdin.readline

C, R = map(int, input().split())

N = int(input())

store = []


def calc_dist(dir, dist):
    if dir == 1:
        return dist
    elif dir == 2:
        return C+R+(C-dist)
    elif dir == 3:
        return C+R+C+(R-dist)
    elif dir == 4:
        return C+dist


for i in range(N+1):
    if i == N:
        direction, distance = map(int, input().split())
    else:
        store.append(list(map(int, input().split())))

answer = 0
dist1 = calc_dist(direction, distance)

for i in range(N):
    dist2 = calc_dist(store[i][0], store[i][1])
    path1 = abs(dist1-dist2)
    path2 = 2 * C + 2 * R - path1
    answer += path1 if path1 < path2 else path2

print(answer)
