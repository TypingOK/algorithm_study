import sys
input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))
M = int(input())
box2 = list(map(int, input().split()))

box.sort()
box2.sort()


def binary_search(start, end, search):
    while start <= end:
        mid = (start + end) // 2
        if box[mid] == search:
            return True
        elif box[mid] > search:
            end = mid - 1
        else:
            start = mid + 1
    return False


for i in range(M):
    if binary_search(0, N, box2[i]):
        print("yes")
    else:
        print("no")
