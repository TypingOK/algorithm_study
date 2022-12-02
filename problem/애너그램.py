from itertools import permutations
import sys

input = sys.stdin.readline


def back(cnt):
    if cnt == len(word):
        print("".join(answer))
        return

    for i in visit:
        if visit[i]:
            visit[i] -= 1
            answer.append(i)
            back(cnt+1)
            visit[i] += 1
            answer.pop()


N = int(input())


for i in range(N):
    word = list(input())
    word.pop()
    word.sort()
    visit = {}
    answer = []

    for i in word:
        if i in visit:
            visit[i] += 1
        else:
            visit[i] = 1
    back(0)
    # print(word)
