import sys

T = int(sys.stdin.readline())
f = [0, 1]
for i in range(2, 46):
    f.append(f[i-2]+f[i-1])

for _ in range(T):
    N = int(sys.stdin.readline())

    answer = []

    for i in range(45, 0, -1):
        if f[i] <= N:
            N -= f[i]
            answer.append(f[i])

            if N == 0:
                answer.sort()
                print(" ".join(map(str, answer)))
                break
