import sys
N = int(sys.stdin.readline())
T = [0]
P = [0]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    T.append(a)
    P.append(b)

dp = [0 for _ in range(N+1)]

for i in range(N+1):
    dp[i] = max(dp[i], dp[i-1])
    end_date = T[i] + i - 1
    if end_date <= N:
        dp[end_date] = max(dp[end_date], dp[i-1]+P[i])
print(max(dp))
