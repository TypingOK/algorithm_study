import sys

input = sys.stdin.readline
N, M = map(int, input().split())

price = []

for i in range(M):
    price.append(int(input()))

price.sort(reverse=True)
max_price = 0

index = 0
answer = 0
while True:
    now_price = 0
    for i in range(M):
        if i < N:
            if price[index] <= price[i]:
                now_price += price[index]
            else:
                break
        else:
            break
    if now_price >= max_price:
        max_price = now_price
        answer = price[index]
    index += 1
    if index == M:
        break
print(answer, max_price)
