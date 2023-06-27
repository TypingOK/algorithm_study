import sys
N, K = map(int, sys.stdin.readline().split())

count = 0
while True:
    temp = (N//K) * K
    count += (N-temp)
    N = temp
    if N < K:
        break
    count += 1
    N //= K

count += (N-1)

print(count)
