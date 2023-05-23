import sys
input = sys.stdin.readline

N = int(input())
b = list(map(int, input().split()))

count = 0
height = [0] * 1000001

for i in b:
    if height[i]:
        height[i] -= 1
    else:
        count += 1
    height[i-1] += 1
print(count)
