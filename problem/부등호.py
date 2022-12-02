import sys
input = sys.stdin.readline

N = int(input())
word = list(input().split())

visit = [False] * 10

cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []


def perf(visit, depth):
    if(depth >= N+1):
        # print(select)

        result.append("".join((str(_) for _ in select)))
        return
    for i in range(10):
        if(not visit[i]):
            # print(word[depth-1], " ", select[depth-1], " ", cards[i])
            if(word[depth-1] == '>' and select[depth-1] > cards[i]):
                # print("test")
                visit[i] = True
                select.append(cards[i])
                perf(visit, depth+1)
                select.pop()
                visit[i] = False
            elif(word[depth-1] == '<' and select[depth-1] < cards[i]):
                visit[i] = True
                select.append(cards[i])
                perf(visit, depth+1)
                select.pop()
                visit[i] = False


for i in range(10):
    visit[i] = True
    select = [cards[i]]
    perf(visit, 1)
    visit[i] = False
print(result[-1])
print(result[0])
