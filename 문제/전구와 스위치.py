from copy import deepcopy
import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().rstrip()))
num2 = deepcopy(num)
num3 = deepcopy(num)

after = list(map(int, sys.stdin.readline().rstrip()))


def two(i, j):
    num[i] = 1-num[i]
    num[j] = 1-num[j]


def three(i, j, k):
    num[i] = 1-num[i]
    num[j] = 1-num[j]
    num[k] = 1-num[k]


cnt = 0
for j in range(N):
    num = num2
    if 1 <= j <= N-2:
        if num[j-1] != after[j-1]:
            cnt += 1
            three(j-1, j, j+1)
    elif j == N-1:
        if(num[j-1] != after[j-1]):
            cnt += 1
            two(j-1, j)
    if num == after:
        print(cnt)
        exit()
cnt = 0
for j in range(N):
    num = num3
    if j == 0:
        if num != after:
            cnt += 1
            two(j, j+1)
    elif 1 <= j <= N-2:
        if num[j-1] != after[j-1]:
            cnt += 1
            three(j-1, j, j+1)
    elif j == N-1:
        if(num[j-1] != after[j-1]):
            cnt += 1
            two(j-1, j)
    if num == after:
        print(cnt)
        exit()
if(num != after):
    print(-1)
