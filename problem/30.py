import sys
input = sys.stdin.readline

N = list(input().rstrip())

N.sort(reverse=True)

if(N[-1] != '0'):
    print(-1)
else:
    temp = ''.join(N)
    temp = int(temp)
    if(temp % 30 ==0):
        print(temp)
    else:
        print(-1)
        
