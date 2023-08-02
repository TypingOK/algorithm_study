import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [A[i] for i in range(N)]

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if A[j] < A[i] and dp[i] < dp[j] + A[i]:
            dp[i] = dp[j] + A[i]

print(max(dp))
