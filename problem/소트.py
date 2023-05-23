import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
S = int(input())

for i in range(N):
    max_number = max(numbers[i:min(N, i+S+1)])
    index = numbers.index(max_number)

    for j in range(index, i, -1):
        numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

    S -= (index-i)
    if S <= 0:
        break

print(" ".join(map(str, numbers)))
