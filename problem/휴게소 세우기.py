import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.append(1)
rest.append(L-1)

rest.sort()
left = rest[0]
right = L


answer = sys.maxsize
while (left <= right):
    mid = (left+right) // 2
    
    count = 0
    for i in range(1,len(rest)):
        count += (rest[i]-rest[i-1]-1)//mid

    if count > M:
        left = mid + 1
    else:
        answer = min(answer, mid)
        right = mid - 1
print(answer)
