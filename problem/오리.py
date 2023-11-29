import sys

input = sys.stdin.readline
S = input().strip("\n")

word = "quack"
temp = ""

answer = 0
while True:
    index = 0
    i = 0
    temp = ""
    flag = False
    while index < len(S):
        if S[index] == word[i]:
            temp += S[index]
            S = S[:index] + S[index+1:]
            index -= 1
            i += 1
        if temp == word:
            flag = True
            temp = ""
            i = 0

        index += 1

    if flag:
        answer += 1

    if S == "" or not flag or temp != "":
        break
if answer == 0 or S != "" or temp != "":
    print(-1)
else:
    print(answer)
