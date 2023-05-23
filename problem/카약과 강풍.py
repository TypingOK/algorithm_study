import sys
input = sys.stdin.readline

N, S, R = map(int, input().split())
b = list(map(int, input().split()))
n = list(map(int, input().split()))
dust = []
b.sort()
n.sort()
for i in range(R):
    if n and n[i] in b:
        b.pop(b.index(n[i]))
        dust.append(i)
dust.sort(reverse=True)
for i in dust:
    n.pop(i)

for i in n:
    if i - 1 in b:
        temp = b.index(i-1)
        b.pop(temp)
    elif i + 1 in b:
        temp = b.index(i+1)
        b.pop(temp)

print(len(b))
