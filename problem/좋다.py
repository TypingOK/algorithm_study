import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

count = 0
for i in range(N):
    temp = A[:i] + A[i+1:]
    start = 0
    end = len(temp)-1

    while (start < end):
        mid = temp[start] + temp[end]

        if mid == A[i]:
            count += 1
            break

        elif mid > A[i]:
            end -= 1
        else:
            start += 1

print(count)
