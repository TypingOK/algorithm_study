import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    a = list(input().rstrip())
    b = list(input().rstrip())
    w_count = 0
    b_count = 0
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] == 'W':
                w_count += 1
            else:
                b_count += 1
    while w_count > 0 and b_count > 0:
        w_count -= 1
        b_count -= 1
        answer += 1
    if w_count > 0:
        answer += w_count
    if b_count > 0:
        answer += b_count
    print(answer)
