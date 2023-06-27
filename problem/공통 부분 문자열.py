from sys import stdin
input = stdin.readline

s1 = input().strip("\n")
s2 = input().strip("\n")

dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0

max_count = 0
for i in dp:
    temp = max(i)
    max_count = max(temp, max_count)
print(max_count)
