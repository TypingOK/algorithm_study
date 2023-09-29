import sys
input = sys.stdin.readline

N, C = map(int, input().split())

numbers = []

for i in range(N):
    numbers.append(int(input()))

numbers.sort()

# 거리를 기준으로 매개 변수 탐색
start = 1
end = numbers[-1] - numbers[0]
answer = 0

while start <= end:
    mid = (start + end)//2

    count = 1
    index = 0
    for i in range(0, N):
        if numbers[i] - numbers[index] >= mid:
            count += 1
            index = i
    if count >= C:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)
