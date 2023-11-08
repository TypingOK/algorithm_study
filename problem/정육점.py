import sys
input = sys.stdin.readline

N, M = map(int, input().split())
meat = []

for i in range(N):
    a, b = map(int, input().split())
    meat.append((a, b))

meat.sort(key=lambda x: (x[1], -x[0]))

count = 0
answer = 2147483647
s = 0
flag = True
for i in range(N):
    count += meat[i][0]
    if i >= 1 and meat[i][1] == meat[i-1][1]:
        s += meat[i][1]
    else:
        s = 0
    if count >= M:
        answer = min(answer, meat[i][1] + s)
        flag = False

if flag:
    print(-1)
else:
    print(answer)
