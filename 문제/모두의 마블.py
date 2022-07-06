import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

maxVal = max(card)
index = card.index(maxVal)
# print(index)

answer = 0

if(index >= 0 and index < N-1):
    for i in range(index+1, N):
        answer += card[i]+maxVal
if(index >= 1):
    for i in range(index-1, -1, -1):
        answer += card[i]+maxVal
print(answer)
