import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())

answer = 0
buy = 0
if(N > M):
    # while(True):
    #     count = 0
    #     temp = N + buy
    #     while(temp > 0):
    #         if(temp % 2 != 0):
    #             count += 1
    #         temp = temp // 2

    #     if(count <= M):
    #         break
    #     buy += 1
    # answer = buy
    for i in range(M-1):
        count = 0
        while(math.pow(2, count) < N):
            count += 1
        N -= math.pow(2, count-1)
        if(N == 0):
            N = 0
            answer = 0
            break
    if(N != 0):
        count = 0

        while(math.pow(2, count) < N):
            count += 1
        answer = int(math.pow(2, count) - N)

print(answer)
