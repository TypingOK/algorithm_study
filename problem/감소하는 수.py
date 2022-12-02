import sys
from collections import deque
N = int(sys.stdin.readline())


result = 0
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
q = deque(number)
count = 9

if(N <= 9):
    print(q[N])
else:
    flag = False
    while q:
        temp = q.popleft()
        for i in range(0, 10):
            if (int(temp[-1]) <= i):
                break
            q.append(temp+str(i))
            count += 1
            if(count >= N):
                print(q[-1])
                exit()
    print(-1)
