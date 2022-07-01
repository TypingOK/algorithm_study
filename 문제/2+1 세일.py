import sys
input = sys.stdin.readline
N = int(input())

milk = []

for i in range(N):
    milk.append(int(input()))

milk.sort(reverse=True)
sum = 0

for i in range(N):
    if((i+1) % 3 == 0):
        continue
    # print(i)
    sum += milk[i]

print(sum)
