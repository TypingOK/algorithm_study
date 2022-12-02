import sys

input = sys.stdin.readline

N = int(input())

temp = []

for i in range(N):
    temp.append(list(map(int, input().split(" "))))

temp.sort(key=lambda x: (x[0], x[1]))
count = 0

for i in temp:
    if(count < i[0]):
        count = i[0] + i[1]
    elif(count >= i[0]):
        count += i[1]

print(count)
