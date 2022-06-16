import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input()
    stack = deque()
    cur = 0
    for i in range(len(s)-1):
        if s[i] == '<':
            if cur == 0:
                continue
            else:
                cur -= 1
        elif s[i] == '>':
            if cur == len(stack):
                continue
            else:
                cur += 1
        elif s[i] == "-":
            if cur == 0:
                continue
            else:
                del stack[cur-1]
                cur -= 1
        else:
            if cur == 0:
                stack.appendleft(s[i])
                cur += 1
            elif cur == len(stack):
                stack.append(s[i])
                cur += 1
            else:
                stack.insert(cur, s[i])
                cur += 1
        # print(stack)
        # print(cur, s[i])
    print(''.join(list(stack)))
