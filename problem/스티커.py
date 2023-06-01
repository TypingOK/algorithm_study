import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    s = []
    for i in range(2):
        temp = list(map(int, input().split()))
        s.append(temp)
    if N > 1:
        s[0][1] += s[1][0]
        s[1][1] += s[0][0]

        for i in range(2, N):
            s[0][i] += max(s[1][i-1], s[1][i-2])
            s[1][i] += max(s[0][i-1], s[0][i-2])
    print(max(s[0][-1], s[1][-1]))
