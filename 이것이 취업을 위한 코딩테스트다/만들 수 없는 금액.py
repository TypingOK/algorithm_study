import sys
N = int(sys.stdin.readline())
coin = list(map(int, sys.stdin.readline().split()))

coin.sort()

index = 1

for i in coin:
    if index < i:
        break
    index += i
print(index)
