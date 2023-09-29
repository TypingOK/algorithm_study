import sys
input = sys.stdin.readline
N = int(input())

numbers = list(map(int, input().split()))

start = 0
end = N - 1
answer = -1

while start <= end:
    mid = (start+end)//2
    print(mid, numbers[mid])
    if mid == numbers[mid]:
        answer = mid
        break
    elif mid < numbers[mid]:
        end = mid - 1
    else:
        start = mid + 1
print(answer)
