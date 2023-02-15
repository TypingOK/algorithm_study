import sys

input = sys.stdin.readline

N, C = map(int, input().split())

home = [int(input()) for _ in range(N)]

home.sort()

# 가능한 거리
left = 1
right = home[-1] - home[0]

while(left <= right):
    mid = (left+right) // 2
    
    count = 1
    start = home[0]
    for i in range(0,len(home)):
        if(home[i] - start >= mid):
            start = home[i]
            count += 1
    if count < C:
        right = mid-1
    else:
        left = mid + 1
print(right)
