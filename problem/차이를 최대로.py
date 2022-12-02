from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

num.sort()

arr = list(permutations(num, n))

answer = 0

for i in range(len(arr)):
    count = 0
    for j in range(0,n-1):
        count += abs(arr[i][j]-arr[i][j-1])
    answer = max(answer,count)

print(answer)