import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
peoples = []

for i in range(N):
    peoples.append(list(map(int, input().split())))

temp = []
for i in range(N):
    max_num = 0
    comb = combinations(peoples[i], 3)
    count = 0
    for j in comb:
        count = (j[0]+j[1]+j[2]) % 10
        max_num = max(max_num, count)
    temp.append(max_num)

max_num = temp[0]

answer = 0

for i in range(N):
    if (temp[i] >= max_num):
        answer = i+1
        max_num = temp[i]

print(answer)
