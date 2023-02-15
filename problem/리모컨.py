import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
crushed = list(map(int, input().split()))

min_count = abs(100 - N)

for i in range(1000001):
    i = str(i)

    for j in range(len(i)):

        if (int(i[j]) in crushed):
            break

        elif (j == len(i) - 1):
            min_count = min(min_count, abs(int(i)-N)+len(i))

print(min_count)
