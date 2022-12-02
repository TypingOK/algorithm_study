import sys
input = sys.stdin.readline

N = int(input())
person = list(map(int, input().split(" ")))

answer = [0] * N

for i in range(1,N+1):

    temp = person[i-1]
    count = 0 

    for j in range(N):
        if count == temp and answer[j] == 0:
            answer[j] = i
            break
        elif answer[j] == 0:
            count += 1


for i in range(N):
    print(answer[i], end=" ")