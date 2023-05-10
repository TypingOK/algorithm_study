import sys
K = int(sys.stdin.readline())

D = 1
count = 0
while D < K:
    D *= 2
temp = D
choco = 0
while D != K and choco != K:
    count += 1
    temp //= 2
    if choco + temp> K:
        continue
    choco += temp


print(D, count)
