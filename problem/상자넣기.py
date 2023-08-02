import sys
input = sys.stdin.readline

N = int(input())
boxs = list(map(int, input().split()))

dp = [1 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    for j in range(0, i):
        if boxs[i] > boxs[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
