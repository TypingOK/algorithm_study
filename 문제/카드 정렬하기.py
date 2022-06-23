import sys
import heapq
input = sys.stdin.readline

N = int(input())

number = []
for i in range(N):
    heapq.heappush(number, int(input()))
answer = 0
while(len(number)) > 1:
    a = heapq.heappop(number)
    b = heapq.heappop(number)
    answer += (a+b)
    heapq.heappush(number, a+b)

print(answer)
