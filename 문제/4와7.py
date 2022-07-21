import sys
input = sys.stdin.readline

K = int(input())

temp = format(K+1, 'b')

answer = ""
for i in temp:
    if i == '0':
        answer+='4'
    else:
        answer+='7'

print(answer[1:])
