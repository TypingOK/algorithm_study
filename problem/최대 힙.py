import sys
import heapq

input = sys.stdin.readline


N = int(input())

number = []
for i in range(N):
    temp = int(input())
    if(temp != 0):
        heapq.heappush(number, (-temp, temp))
    elif(temp == 0):
        if(not number):
            print(0)
        else:
            b = heapq.heappop(number)[1]
            print(b)
