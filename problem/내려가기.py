import sys
input = sys.stdin.readline

N = int(input())
grid = []


dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

grid.append(list(map(int, input().split())))

for i in range(3):
    dp_max[i] = grid[0][i]
    dp_min[i] = grid[0][i]

for _ in range(1, N):
    temp = list(map(int, input().split()))
    dp_temp_max = [0, 0, 0]
    dp_temp_max[0] = max(dp_max[0] + temp[0], dp_max[1] + temp[0])
    dp_temp_max[1] = max(dp_max[0] + temp[1], dp_max[1] +
                         temp[1], dp_max[2] + temp[1])
    dp_temp_max[2] = max(dp_max[1] + temp[2], dp_max[2] + temp[2])
    dp_max[0] = dp_temp_max[0]
    dp_max[1] = dp_temp_max[1]
    dp_max[2] = dp_temp_max[2]

    dp_temp_min = [0, 0, 0]
    dp_temp_min[0] = min(dp_min[0] + temp[0], dp_min[1] + temp[0])
    dp_temp_min[1] = min(dp_min[0] + temp[1], dp_min[1] +
                         temp[1], dp_min[2] + temp[1])
    dp_temp_min[2] = min(dp_min[1] + temp[2], dp_min[2] + temp[2])
    dp_min[0] = dp_temp_min[0]
    dp_min[1] = dp_temp_min[1]
    dp_min[2] = dp_temp_min[2]

print(max(dp_max), min(dp_min))
