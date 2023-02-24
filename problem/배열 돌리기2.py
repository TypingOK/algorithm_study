import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())

numbers = []

for i in range(N):
    temp = list(map(int, input().split()))
    numbers.append(temp)

turns = []
cur = min(N, M)

for k in range(cur//2):
    turns.append(2*((N-(2*k))+(M-(2*k)))-4)


for i in range(cur//2):
    for k in range(R % turns[i]):
        temp = numbers[i][i]
        for j in range(i, M-i-1):
            numbers[i][j] = numbers[i][j+1]
        for j in range(i, N-i-1):
            numbers[j][M-i-1] = numbers[j+1][M-i-1]
        for j in range(M-i-1, i-1, -1):
            numbers[N-1-i][j] = numbers[N-1-i][j-1]
        for j in range(N-i-1, i, -1):
            numbers[j][i] = numbers[j-1][i]
        numbers[i+1][i] = temp
for i in range(N):
    for j in range(M):
        print(numbers[i][j], end=" ")
    print()
