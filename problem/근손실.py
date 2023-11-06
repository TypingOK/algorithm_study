import sys
power = 500
input = sys.stdin.readline

N, K = map(int, input().split())
health = list(map(int, input().split()))
visited = [False] * N
answer = 0


def re(count, visited, depth, K):
    global answer
    if count < 500:
        return
    if depth >= N:
        answer += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            re(count - K + health[i], visited, depth+1, K)
            visited[i] = False


re(500, visited, 0, K)
print(answer)
