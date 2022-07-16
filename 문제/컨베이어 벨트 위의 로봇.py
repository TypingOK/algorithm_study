import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split(" "))

belt = deque(list(map(int, input().split(" "))))

N -= 1

index = 0

check = deque([False] * len(belt))


while(True):
    index += 1
    belt.rotate(1)
    check.rotate(1)
    if(check[N]):
        check[N] = False

    for i in range(N-1, -1, -1):
        if(check[i] and belt[i+1] > 0 and not check[i+1]):
            check[i+1] = True
            belt[i+1] -= 1
            check[i] = False
    if(check[N]):
        check[N] = False

    if(not check[0] and belt[0] > 0):
        check[0] = True
        belt[0] -= 1
    count = 0
    for i in range(len(belt)):
        if(belt[i] == 0):
            count += 1
    if(count >= K):
        break
print(index)
