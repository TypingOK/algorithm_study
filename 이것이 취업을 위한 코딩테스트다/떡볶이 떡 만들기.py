import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rice = list(map(int, input().split()))

answer = 0


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start+end) // 2
        count = 0
        for i in range(N):
            if rice[i] > mid:
                count += rice[i] - mid

        if count >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


answer = binary_search(0, max(rice))
print(answer)
