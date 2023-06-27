import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

count = 0
answer = 0
for i in range(M):
    if count < K:
        answer += numbers[0]
        count += 1
    else:
        answer += numbers[1]
        count = 0

print(answer)
