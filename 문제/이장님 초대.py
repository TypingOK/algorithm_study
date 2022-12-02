N = int(input())
answer = list(map(int, input().split()))
answer.sort(reverse=True)
for i in range(N):
    answer[i] = answer[i]+i + 1
print(max(answer)+1)