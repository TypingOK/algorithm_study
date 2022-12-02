import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
point = list(map(int, input().split(" ")))

if N <= K:
    print(0)
else:
    point.sort()
    dist = []
    for i in range(1, N):
        dist.append(abs(point[i]-point[i-1]))
    dist.sort()

    for i in range(K-1):
        dist.pop()
    print(sum(dist))
