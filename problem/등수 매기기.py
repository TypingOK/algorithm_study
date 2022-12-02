import sys
input = sys.stdin.readline

N = int(input())
rank = []

for i in range(N):
    rank.append(int(input()))
rank.sort()
answer = 0
for i in range(1, N+1):
    answer += abs(rank[i-1]-i)
print(answer)
