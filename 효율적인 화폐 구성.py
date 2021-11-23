N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(int(input()))
d = [10001]*101
d[0] = 0

for i in range(N):
    for j in range(array[i], M+1):
        d[j] = min(d[j], d[j-array[i]]+1)
if d[M] == 10001:
    print(-1)
else:
    print(d[M])
