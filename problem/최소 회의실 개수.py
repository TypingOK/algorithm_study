import sys
import heapq
input = sys.stdin.readline

N = int(input())
room = []
for i in range(N):
    room.append(list(map(int, input().split())))

room.sort()
h = []
for i in range(N):
    if len(h) == 0:
        heapq.heappush(h, room[i][1])
    else:
        result = h[0]
        if room[i][0] >= result:
            heapq.heappop(h)
            heapq.heappush(h,  room[i][1])
        else:
            heapq.heappush(h,  room[i][1])

print(len(h))
