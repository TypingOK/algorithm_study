import sys
input = sys.stdin.readline

N, K = map(int, input().split())
x = list(map(int, input().split()))

left = min(x)
right = sum(x)
answer = 98765432119999

while (left < right):
    mid = (left + right)//2
    count = 0
    grade = 0
    for i in range(N):
        grade += x[i]
        if grade >= mid:
            count += 1
            grade = 0
    if count >= K:
        answer = mid
        left =  mid + 1
    elif count < K:
        right =  mid - 1
print(answer)
