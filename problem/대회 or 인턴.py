import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

count = 0
while K > 0:
    if N >= 2 * M:
        K -= 1
        N -= 1
    elif N < 2 * M:
        M -= 1
        K -= 1

N //= 2

count = min(N, M)
print(count)
