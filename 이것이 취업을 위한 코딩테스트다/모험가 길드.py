import sys
input = sys.stdin.readline

N = int(input())
peoples = list(map(int, input().split()))
peoples.sort()

index = 0
result = 0

for i in peoples:
    index += 1
    if index >= i:
        result += 1
        index = 0
print(result)
