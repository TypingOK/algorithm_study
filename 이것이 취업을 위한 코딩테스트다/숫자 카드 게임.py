import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = []

for i in range(N):
    cards.append(list(map(int, input().split())))

numbers = []
for i in cards:
    min_num = min(i)

    numbers.append(min_num)

print(max(numbers))
