import sys

input = sys.stdin.readline

N = int(input())

color = list(map(str, input().rstrip()))

red = color.count('R')
blue = N - red


answer = min(red, blue)

count = 0
for i in range(N):
    if color[0] != color[i]:
        break
    count += 1

if(color[0] == 'R'):
    answer = min(answer, red-count)
else:
    answer = min(answer, blue-count)

count = 0
for i in range(N-1, -1, -1):
    if color[N-1] != color[i]:
        break
    count += 1

if(color[N-1] == 'R'):
    answer = min(answer, red-count)
else:
    answer = min(answer, blue-count)

print(answer)
