import sys
input = sys.stdin.readline

N, W = map(int, input().split())

days = [int(input()) for _ in range(N)]
buy = 0

for i in range(1, len(days)):
    if buy > 0:
        if days[i] < days[i-1]:
            W += (buy * days[i-1])
            buy = 0
    else:
        if days[i] > days[i-1]:
            buy = (W // days[i-1])
            W = W % days[i-1]

if buy > 0:
    W += (buy * days[-1])
print(W)
