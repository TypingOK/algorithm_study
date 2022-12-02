import sys

input = sys.stdin.readline

N = int(input())

list1 = []
for i in range(N):
    list1.append(int(input()))

score = list1[N-1]
answer = 0
for i in range(N-2, -1, -1):
    while(list1[i] >= score):
        answer += 1
        list1[i] -= 1
    score = list1[i]


print(answer)
