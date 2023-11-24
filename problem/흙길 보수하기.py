import sys
input = sys.stdin.readline

N, L = map(int, input().split())
water = []

for i in range(N):
    water.append(list(map(int, input().split())))

water.sort(key=lambda x: (x[0]))

answer = 0
pan = water[0][0]

for i in water:
    if pan > i[1]:
        continue
    elif pan < i[0]:
        pan = i[0]

    dist = i[1] - pan
    remainder = 1

    if dist % L == 0:
        remainder = 0

    count = dist // L + remainder
    pan += count * L
    answer += count
print(answer)
