import heapq
import sys
input = sys.stdin.readline

q = []

N = int(input())

for i in range(N):
    temp = int(input())
    if(temp != 0):
        heapq.heappush(q,temp)
    else:
        if(len(q)!=0):
            print(heapq.heappop(q))
        else:
            print(0)





