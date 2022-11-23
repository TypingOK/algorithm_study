import sys
from collections import deque
input = sys.stdin.readline

N, A, B = map(int, input().split())

a_tile = list(map(int, input().split()))
b_tile = list(map(int, input().split()))

a_tile.sort(reverse=True)
b_tile.sort(reverse=True)

a_tile = deque(a_tile)
b_tile = deque(b_tile)

count = 0
if(N % 2 == 1):
    count += a_tile.popleft()
    A -= 1
    N -= 1
while(N > 0):
    if(N > 1):
        if(A >= 2 and B >= 1 and a_tile[0]+a_tile[1] > b_tile[0]):
            count += a_tile.popleft()
            count += a_tile.popleft()
            A -= 2
            N -= 2
        elif(A >= 2 and B >= 1 and a_tile[0]+a_tile[1] < b_tile[0]):
            count += b_tile.popleft()
            B -= 1
            N -= 2
        elif(A >= 2 and B >= 1 and a_tile[0]+a_tile[1] == b_tile[0]):
            if(A-2 >= B-1):
                count += a_tile.popleft()
                count += a_tile.popleft()
                A -= 2
                N -= 2
            else:
                count += b_tile.popleft()
                B -= 1
                N -= 2
        elif(B == 0):
            count += a_tile.popleft()
            count += a_tile.popleft()
            A -= 2
            N -= 2
        elif(A == 1 or A == 0):
            count += b_tile.popleft()
            B -= 1
            N -= 2

print(count)
