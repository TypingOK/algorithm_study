import sys
input = sys.stdin.readline

N = int(input())
number = []

for i in range(N):
    number.append(int(input()))

print(round(sum(number)/N))
number.sort()
print(number[len(number)//2])
temp = dict()
for i in number:
    if i in temp:
        temp[i] += 1
    else:
        temp[i] = 1

result = sorted(temp.items(), key=lambda x: x[1], reverse=True)
if len(result) > 1 and result[0][1] == result[1][1]:
    print(result[1][0])
else:
    print(result[0][0])

print(number[-1] - number[0])
