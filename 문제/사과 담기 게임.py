import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

J = int(input())

apples = []

for j in range(J):
    apples.append(int(input()))
answer = 0
index = 1
for i in apples:
    count = 0
    while True:
        if(index <= i <= index + M - 1):
            answer += count
            break
        if(index > i):
            count += 1
            index -= 1
        else:
            index += 1
            count += 1
print(answer)
