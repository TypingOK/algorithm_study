import sys
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split(" "))

ak = int(input())

do = []
for i in range(N):
    do.append(int(input()))

do.sort(reverse=True)

money = a
kcal = ak

index = 1
for i in do:
    tempMoney = money+b
    tempkcal = kcal + i
    if((tempkcal//tempMoney) >= (kcal//money)):
        money = tempMoney
        kcal = tempkcal
        index += 1
    else:
        break

print(kcal//money)
