import sys
sys.setrecursionlimit(10**6)

S1 = sys.stdin.readline().rstrip("\n")
S2 = sys.stdin.readline().rstrip("\n")

dp = [[0 for _ in range(len(S2)+1)] for _ in range(len(S1)+1)]

for i in range(1, len(S1)+1):
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

answer = ""


def backtracking(dp, S1, S2, i, j):
    global answer
    if dp[i][j] == 0:
        return
    elif S1[i-1] == S2[j-1]:
        answer += S1[i-1]
        return backtracking(dp, S1, S2, i-1, j-1)
    else:
        if dp[i-1][j] <= dp[i][j-1]:
            return backtracking(dp, S1, S2, i, j-1)
        else:
            return backtracking(dp, S1, S2, i-1, j)


backtracking(dp, S1, S2, len(S1), len(S2))
print(dp[-1][-1])
print("".join(reversed(answer)))
