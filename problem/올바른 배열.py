import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers.sort()
answer = 5

for i in range(N):
    count = 0
    for j in range(numbers[i], numbers[i]+5):
        if j in numbers:
            count += 1

    answer = min(5 - count, answer)
if answer < 0:
    print(0)
else:
    print(answer)
