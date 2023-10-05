import sys
input = sys.stdin.readline
N = int(input())

T = []
P = []

for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i+T[i], N+1):
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]

print(dp[-1])
