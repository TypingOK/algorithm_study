import sys

input = sys.stdin.readline

N = int(input())
me = int(input())

other = []

for i in range(N-1):
    other.append(int(input()))

count = 0

while True:
    maxNum = 0
    index = 0
    for i in range(len(other)):
        if(maxNum < other[i]):
            maxNum = other[i]
            index = i
    if(me>maxNum):
        break
    else:
        other[index] -= 1
        me += 1
        count += 1
print(count)