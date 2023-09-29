import sys
input = sys.stdin.readline


def count_by_value(array, x):
    n = len(array)

    a = first(array, x, 0, n-1)

    if a == None:
        return 0

    b = last(array, x, 0, n-1)

    return b-a+1


def first(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if (mid == N-1 or target < array[mid+1]) and array[mid] == target:
        return mid

    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)


N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# start = 0
# end = len(numbers) - 1

# answer = -1
# while start < end - 1:
#     mid = (start + end) // 2

#     if numbers[mid] == M:
#         answer = numbers.count(numbers[mid])
#         break
#     elif numbers[mid] > M:
#         end = mid-1
#     elif numbers[mid] < M:
#         start = mid + 1

# print(answer)

count = count_by_value(numbers, M)
if count == 0:
    print(-1)
else:
    print(count)
