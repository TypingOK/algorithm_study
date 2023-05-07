import sys

input = sys.stdin.readline
N, K = map(int, input().split())

number = list(map(int, input().split()))
sorted_number = sorted(number, reverse=True)
sorted_number = sorted_number[:K]
answer = 0
count = 0
for i in range(N):
    if number[i] in sorted_number:
        answer += (number[i] - count)
        index = sorted_number.index(number[i])
        sorted_number.pop(index)
        count += 1
    if count == K:
        break

print(answer)
