import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    box = []
    for _ in range(N):
        A, B = map(int, input().split())
        box.append(A*B)

    box.sort(reverse=True)
    count = 0
    index = 0
    while True:
        if J > 0:
            J -= box[index]
            index += 1
            count += 1
        else:
            break
    print(count)
