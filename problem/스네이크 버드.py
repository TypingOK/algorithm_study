import sys
input = sys.stdin.readline

N,L = map(int,input().split())

f = list(map(int,input().split()))
f.sort()

for i in range(N):
    if(f[i]<=L):
        L+=1
print(L)