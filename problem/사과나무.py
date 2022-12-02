import sys
input = sys.stdin.readline

N = int(input())
tree = list(map(int,input().split(" ")))

total = sum(tree)

if(total % 3 != 0):
    print("NO")
else:
    cnt = 0
    temp = total // 3

    for i in range(N):
        cnt+=tree[i]//2
    
    if cnt>=temp:
        print("YES")
    else:
        print("NO")