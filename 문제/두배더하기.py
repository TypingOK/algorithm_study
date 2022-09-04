import sys

input = sys.stdin.readline
N = int(input())

B = list(map(int, input().split(" ")))

count = 0
B.sort()
while(True):
    check = False
    complete = False
    complete_check = 0
    for i in range(N):
        if(B[i] == 0):
            complete_check += 1
        if(B[i] % 2 == 1):
            B[i] -= 1
            count += 1
            check = True
    if(complete_check == N):
        break
    if(not check):
        for i in range(N):
            B[i] = B[i] // 2
        count += 1
print(count)
