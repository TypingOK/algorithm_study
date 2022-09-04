import sys

input = sys.stdin.readline

N, X = map(int, input().split(" "))

taste = []
answer = 0
for i in range(N):
    taste.append(list(map(int, input().split(" "))))
    answer += taste[i][1]

taste.sort(key=lambda x: (x[0]-x[1]), reverse=True)
X -= 1000 * N
for i in taste:
    if X >= 4000 and i[0] > i[1]:
        answer += (i[0] - i[1])
        X -= 4000
    else:
        break
print(answer)
