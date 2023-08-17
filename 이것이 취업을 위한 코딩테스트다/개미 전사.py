import sys
input = sys.stdin.readline

N = int(input())
eatting = [0] + list(map(int, input().split()))
dp = [0 for i in range(N+1)]
dp[1] = eatting[1]
dp[2] = max(eatting[1], eatting[2])

for i in range(3, N+1):
    dp[i] = max(dp[i-2]+eatting[i], dp[i-1])
print(max(dp))
