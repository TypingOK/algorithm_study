import sys
input = sys.stdin.readline

M = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = -sys.maxsize

if M % 2 == 0:
    for i in range(M//2):
        answer = max((arr[i]+arr[M-1-i]), answer)
else:
    for i in range(M//2-1):
        answer = max((arr[i]+arr[M-2-i]), answer)
    answer = max((arr[-1]), answer)
print(answer)
