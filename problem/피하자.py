import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))

r_count = 0
l_count = 0
p = 0

for i in numbers:
    if i % 2 == 1:
        p += 1
    else:
        l_count += p
numbers.reverse()
p=0

for i in numbers:
    if i % 2 == 1:
        p +=1
    else:
        r_count += p
print(min(l_count,r_count))