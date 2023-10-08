import sys
input = sys.stdin.readline

word1 = list(input().rstrip("\n"))
word2 = list(input().rstrip("\n"))

dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
for i in range(1, len(word2)+1):
    dp[0][i] = i
for j in range(1, len(word1)+1):
    dp[j][0] = j

for i in range(1, len(word1)+1):
    for j in range(1, len(word2)+1):
        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])

print(dp[len(word1)-1][len(word2)-1])
