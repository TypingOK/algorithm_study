import sys
input = sys.stdin.readline
N = int(input())
numberic = list(map(int, input().split()))

dp = [1 for i in range(N)]
dp_2 = [1 for i in range(N)]

for i in range(1, N):

    if numberic[i-1] <= numberic[i] and dp[i] < dp[i-1] + 1:
        dp[i] = dp[i-1] + 1

    if numberic[i-1] >= numberic[i] and dp_2[i] < dp_2[i-1] + 1:
        dp_2[i] = dp_2[i-1] + 1
print(max(max(dp), max(dp_2)))
