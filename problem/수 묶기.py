import sys

input = sys.stdin.readline

N = int(input())

number = []

for i in range(N):
    number.append(int(input()))

minus = []
zero = 0
plus = []

for i in number:
    if(i < 0):
        minus.append(i)
    elif(i == 0):
        zero = 1
    else:
        plus.append(i)

minus.sort()
plus.sort(reverse=True)

answer = 0

if(len(minus) % 2 == 1):
    for i in range(1, len(minus)-1, 2):
        answer += (minus[i-1] * minus[i])
    if(zero == 0):
        answer += minus[-1]
    else:
        zero = 9999
elif(len(minus) % 2 == 0):
    for i in range(1, len(minus), 2):
        answer += (minus[i-1] * minus[i])
for i in range(0, len(plus)-1, 2):
    if(plus[i] == 1):
        answer += 2
    elif(plus[i+1] == 1):
        answer += (plus[i])
        answer += 1
    else:
        answer += (plus[i]*plus[i+1])
if(len(plus) % 2 == 1):
    answer+=plus[-1]

print(answer)
