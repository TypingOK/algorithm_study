import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
cards = []

for i in range(N):
    heappush(cards,int(input()))
answer = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)
    answer += (a+b)
    heappush(cards, a+b)
print(answer)
