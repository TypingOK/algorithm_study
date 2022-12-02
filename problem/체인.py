import sys

input = sys.stdin.readline

N = int(input())
M = list(map(int, input().split(" ")))


def cal(N, M):
    M.sort()

    count = 1

    for i in M:
        if count + i >= N:
            break
        else:
            count += i
            N -= 1
    return N-1


answer = cal(N, M)
print(answer)
