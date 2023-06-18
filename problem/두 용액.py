import sys

input = sys.stdin.readline

N = int(input())
water = list(map(int, input().split()))

water.sort()
if water[0] >= 0:
    print(water[0], water[1])

elif water[-1] <= 0:
    print(water[-2], water[-1])

else:
    end = N - 1
    start = 0
    min_number = 987654321000
    answer_left, answer_right = 0, N-1
    while start < end:

        temp = water[start] + water[end]
        if abs(temp) < min_number:
            min_number = abs(temp)
            answer_left = water[start]
            answer_right = water[end]
        if temp < 0:
            start += 1
        elif temp >= 0:
            end -= 1
    print(answer_left, answer_right)
