answer = 0

N, K = list(map(int, input().split()))

while N > 1:

    if N % K != 0:
        N -= 1

    else:
        N //= K
    answer += 1
print(answer)
