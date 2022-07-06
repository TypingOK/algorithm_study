import sys
input = sys.stdin.readline

N = int(input())
enter = {}
for i in range(N):
    car = input()
    enter[car] = i

out = []

for i in range(N):
    car = input()
    out.append(car)

answer = 0

for i in range(N-1):
    for j in range(i+1, N):
        if enter[out[i]] > enter[out[j]]:
            answer += 1
            break

print(answer)
