import sys
input = sys.stdin.readline
N = int(sys.stdin.readline())
m = []

for i in range(N):
    m.append(int(input()))

m.sort(reverse=True)
start = 0
end = 3
answer = -1
while True:
    cur = m[start:end]
    if cur[0] < cur[1]+cur[2]:
        answer = cur[2]+cur[1]+cur[0]
        break
    start += 1
    end += 1
    if end > N:
        break

print(answer)
