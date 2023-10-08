import sys
input = sys.stdin.readline
N = int(input())

# numbers = [1, 2, 3, 4, 5]
# index = 6
# while True:
#     if index / 2 in numbers or index / 3 in numbers or index / 5 in numbers:
#         numbers.append(index)
#     index += 1
#     if len(numbers) >= N:
#         break
# print(numbers[N-1])

ugly = [0 for _ in range(N)]
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, N):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[N-1])
