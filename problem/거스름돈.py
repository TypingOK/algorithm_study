import sys

input = sys.stdin.readline

N = int(input())

count = 0

while(N > 0):
    if(N % 5 == 0):
        count += N//5
        break
    else:
        N -= 2
        count += 1
if(N < 0):
    print(-1)
else:
    print(count)
