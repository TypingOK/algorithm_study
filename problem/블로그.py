import sys
input = sys.stdin.readline

N, X = map(int, input().split())
guest = list(map(int, input().split()))
count = 1
max_num = sum(guest[:X])

start = 1
end = X
num = max_num
while end < N:
    num = num - guest[start-1] + guest[end]
    if num > max_num:
        count = 1
        max_num = num
    elif num == max_num:
        count += 1
    start += 1
    end += 1

if (max_num == 0):
    print("SAD")
else:
    print(max_num)
    print(count)
