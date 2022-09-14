import sys

input = sys.stdin.readline

N = int(input())
peoples = []

for i in range(N):
    peoples.append(int(input()))

peoples.sort(reverse=True)
answer = 0
for i in range(N):
    temp = peoples[i] - i
    if(temp >= 0):
        answer += temp
    else:
        break

print(answer)
