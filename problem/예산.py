import sys

input = sys.stdin.readline

N = int(input())
citys = list(map(int,input().split()))
M = int(input())
citys.sort()
left = citys[0]
right = max(citys)
answer = 0

while(left  <= right):
    mid = (left+right)//2
    count = 0
    for i in citys:
        if i<=mid:
            count += i
        else:
            count += mid
    if count<=M:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)
