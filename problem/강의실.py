import heapq
import sys

input = sys.stdin.readline

n = int(input())

number = []

for i in range(n):
    temp = list(map(int, input().split(" ")))
    number.append(temp)

number.sort(key=lambda x: (x[1], x[2], x[0]))

# print(number)

heap = []

heapq.heappush(heap, number[0][2])
for i in range(1, n):
    if(heap[0] <= number[i][1]):
        heapq.heappop(heap)

    heapq.heappush(heap, number[i][2])
# print(heap)
print(len(heap))
