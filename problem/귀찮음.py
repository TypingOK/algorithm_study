import sys
input = sys.stdin.readline

N = int(input())
sticks = list(map(int, input().split()))

sticks.sort()
answer = 0
sum_sticks = sum(sticks)

for i in range(N):
    answer += ((sum_sticks-sticks[i]) * sticks[i])
    sum_sticks -= sticks[i]
print(answer)
