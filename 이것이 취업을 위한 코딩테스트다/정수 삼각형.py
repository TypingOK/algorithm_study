import sys
input = sys.stdin.readline

N = int(input())

triangle = []
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    triangle.append(temp)

dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(len(triangle[i])):
        if j > 0:
            dp[i][j] = max(dp[i-1][j] + triangle[i][j],
                           dp[i-1][j-1]+triangle[i][j])
        else:
            dp[i][j] = dp[i-1][j] + triangle[i][j]

print(max(dp[-1]))
