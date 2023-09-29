import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = []
    golds = list(map(int, input().split()))
    for i in range(N):
        temp = []
        for j in range(M):
            temp.append(golds[(i*M)+j])
        graph.append(temp)

    dp = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        dp[i][0] = graph[i][0]

    for j in range(1, M):
        for i in range(N):
            if i == 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + graph[i]
                               [j], dp[i+1][j-1] + graph[i][j])
            elif 0 < i < N-1:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + graph[i][j],
                               dp[i][j-1] + graph[i][j], dp[i+1][j-1] + graph[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + graph[i]
                               [j], dp[i][j-1] + graph[i][j])
    max_num = 0
    for i in range(N):
        max_num = max(max_num, dp[i][-1])
    print(max_num)
