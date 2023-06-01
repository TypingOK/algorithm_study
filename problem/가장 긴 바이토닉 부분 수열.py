import sys
input = sys.stdin.readline
N = int(input())

S = list(map(int, input().split()))

lower = [1 for i in range(N)]
upper = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if S[i] > S[j]:
            upper[i] = max(upper[i], upper[j] + 1)
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if S[i] > S[j]:
            lower[i] = max(lower[i], lower[j]+1)
answer = 0

for i in range(N):
    answer = max(answer, (upper[i] + lower[i]))
print(answer-1)
