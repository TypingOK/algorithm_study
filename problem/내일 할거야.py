import sys
input = sys.stdin.readline

N = int(input())
h = []

for i in range(N):
    temp = list(map(int, input().split()))
    h.append(temp)
h.sort(key=lambda x: x[1],reverse=True)

result = h[0][1]
for i in range(N):
    if result >= h[i][1]:
        result = h[i][1] - h[i][0]
    else:
        result = result - h[i][0]
print(result)
