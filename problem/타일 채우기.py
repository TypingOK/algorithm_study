import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(32)]

dp[2] = 3

for i in range(4, 32):
    if i % 2 == 0:
        dp[i] += dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += 2 * dp[j]
        dp[i] += 2

print(dp[N])
