import sys
input = sys.stdin.readline

N = input().rstrip('\n')

word = input().rstrip('\n')

len_word = len(word)
answer = []
for i in N:
    answer += i
    if word == "".join(answer[-len(word):]):
        for _ in range(len_word):
            answer.pop()

if len(answer) > 0:
    print("".join(answer))
else:
    print("FRULA")
