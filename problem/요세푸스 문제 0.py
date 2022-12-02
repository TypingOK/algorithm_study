from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

people = deque([i+1 for i in range(N)])

answer = []
while(people):
    people.rotate(-1 * (M-1))
    answer.append(people.popleft())
answerStr = "<"


# join을 이용하면 좀 더 손쉽게 정답을 출력 할 수 있다.
for i in range(len(answer)-1):
    answerStr += str(answer[i])+", "
answerStr += str(answer[-1])+">"

print(answerStr)
