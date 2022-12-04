import sys

input = sys.stdin.readline
N, M = map(int, input().split())

A = []

for _ in range(N):
    number = list(map(int, input().split()))
    A.append(number)

M, K = map(int, input().split())

B = []

for _ in range(M):
    number = list(map(int, input().split()))
    B.append(number)


C = []


for i in range(N):
    number = []
    for k in range(K):
        count = 0
        for j in range(M):
            count += A[i][j] * B[j][k]
        number.append(count)
    C.append(number)

for i in range(N):
    for j in range(K):
        print(C[i][j], end=" ")
    print()
