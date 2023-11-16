import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for i in range(N):
    A[i] -= B

for i in range(N):
    if A[i] <= 0:
        continue
    else:
        if A[i] % C != 0:
            answer += ((A[i]//C)+1)
        else:
            answer += (A[i]//C)
print(answer)
