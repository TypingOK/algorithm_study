import sys
from collections import deque

input = sys.stdin.readline

D, N = map(int, input().split())

ovens = list(map(int, input().split()))
pizzas = deque(map(int, input().split()))

index = 0

for i in range(D-1):
    if ovens[i] < ovens[i+1]:
        ovens[i+1] = ovens[i]

for i in range(D-1, -1, -1):
    if pizzas[index] <= ovens[i]:
        index += 1
    if index == N:
        print(i+1)
        break
if index != N:
    print(0)
