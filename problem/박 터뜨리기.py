import sys
input = sys.stdin.readline
N, K = map(int, input().split())

if N >= K*(K+1)//2:
    if (N - (K*(K+1)//2)) % K == 0:
        print(K-1)
    else:
        print(K)
else:
    print(-1)
