N,M = list(map(int,input().split()))
card = []
answer=[]
for i in range(N):
    card.append(list(map(int, input().split())))
print(card)

for i in range(N):
    answer.append(min(card[i]))
print(max(answer))
