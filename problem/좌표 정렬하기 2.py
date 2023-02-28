import sys

input = sys.stdin.readline

N = int(input())
position = []

for i in range(N):
    temp = list(map(int, input().split()))
    position.append(temp)


position.sort(key=lambda x: (x[1],x[0]))

for x, y in position:
    print(x, y)
