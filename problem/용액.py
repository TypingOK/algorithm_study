import sys
input = sys.stdin.readline
N = int(input())

water = list(map(int, input().split()))

left = 0
right = N-1
answer_left = 0
answer_right = N-1
answer = sys.maxsize

while left < right:
    temp = water[left] + water[right]

    if abs(temp) < answer:
        answer_right = water[right]
        answer_left = water[left]
        answer = abs(temp)
    if temp >= 0:

        right -= 1
    elif temp < 0:
        left += 1

print(answer_left, answer_right)
