import sys
input = sys.stdin.readline

N, K = map(int, input().split(" "))
child = list(map(int, input().split(" ")))

temp = []
for i in range(1, N):
    temp.append(child[i]-child[i-1])

temp.sort()

answer = 0
for i in range(N-K):
    answer += temp[i]

print(answer)
