import sys

input = sys.stdin.readline


def search(mid, temp, check):
    start = 0
    end = len(temp)-1

    while end-start >= 0:
        if(check == temp[mid]):
            return True
        elif(temp[mid] < check):
            start = mid+1
            mid = (start + end) // 2
        else:
            end = mid-1
            mid = (start + end) // 2
    return False


N = int(input())

temp = list(map(int, input().split(" ")))

M = int(input())

check_list = list(map(int, input().split(" ")))

temp.sort()

answer = []

for i in range(M):
    result = search(N//2, temp, check_list[i])
    if(result):
        answer.append(1)
    else:
        answer.append(0)

print(' '.join(map(str,answer)))
