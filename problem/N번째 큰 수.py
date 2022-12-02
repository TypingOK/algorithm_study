import sys
import heapq
input = sys.stdin.readline

N = int(input())

number = list(map(int,input().split(" ")))
heapq.heapify(number)

for i in range(N-1):
    temp = list(map(int,input().split(" ")))
    for j in temp:
        if(number[0]<j):
            heapq.heappop(number)
            heapq.heappush(number,j)
print(number[0])