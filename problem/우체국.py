import sys
input = sys.stdin.readline

N = int(input())
m = []

people = 0
for i in range(N):
    temp = list(map(int, input().split()))
    m.append(temp)
    people += temp[1]

m.sort(key=lambda x: x[0])
count = 0
result = people/2
for i in range(N):
    count += m[i][1]
    if count >= result:
        print(m[i][0])
        break
