import sys
from collections import deque

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

index = 0
v = [-1 for _ in range(N+1)]
max_count = 0

dp = [1 for _ in range(N+1)]
for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            if dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                v[i] = j
    if (max_count < dp[i]):
        max_count = dp[i]
        index = i

print(max_count)
answer = deque()
while v[index] != -1:
    answer.appendleft(numbers[index])
    index = v[index]
answer.appendleft(numbers[index])
print(" ".join(map(str, answer)))
