import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))
dp = [sys.maxsize for i in range(10001)]
dp[0] = 0

for coin in coins:
    for i in range(coin, 10001):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[K] == sys.maxsize:
    print(-1)
else:
    print(dp[K])
