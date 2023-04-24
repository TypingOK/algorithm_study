import sys
sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
cur = abs(A-B)

answer = 0
for i in range(N):
    f = int(input())
    temp = abs(f-B)
    if cur > temp:
        cur = temp
        A = f
        answer = 1
while A > B:
    A -= 1
    answer += 1

while A < B:
    A += 1
    answer += 1

print(answer)
