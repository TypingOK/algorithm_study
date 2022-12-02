import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

bee = list(map(int, input().split(" ")))
copyBee = deepcopy(bee)

answer = 0

for i in range(1, N):
    copyBee[i] += copyBee[i-1]

for i in range(1, N-1):
    answer = max(answer, 2*copyBee[-1]-bee[0]-copyBee[i]-bee[i])

for i in range(1, N-1):
    answer = max(answer, copyBee[-1]-bee[-1]-bee[i]+copyBee[i-1])

for i in range(1, N-1):
    answer = max(answer, copyBee[i]-bee[0]+copyBee[-1]-copyBee[i-1]-bee[-1])

print(answer)
