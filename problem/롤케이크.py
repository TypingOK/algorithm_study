from collections import deque
import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
cake = list(map(int, input().split()))

cake = sorted(sorted(cake, key=lambda x: x//10), key=lambda x: x % 10)
cake = deque(list(map(int, cake)))


index = 0
count = 0
while(len(cake) != 0):
    if(cake[0] == 10):
        count += 1
        cake.popleft()
    elif(cake[0] > 10):
        if(index == n[1]):
            break
        index += 1
        cake[0] -= 10
        count += 1
    elif(cake[0] < 10):
        cake.popleft()
print(count)
