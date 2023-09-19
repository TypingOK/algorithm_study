import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
T = list(map(int, input().split()))

max_answer = -sys.maxsize
min_answer = sys.maxsize


def dfs(depth, count, N):
    global max_answer
    global min_answer

    if depth >= N:
        max_answer = max(max_answer, count)
        min_answer = min(min_answer, count)

        return
    Flag = False

    for i in range(4):
        if T[i] != 0:
            Flag = True

    if not Flag:
        max_answer = max(max_answer, count)
        min_answer = min(min_answer, count)
        return

    for i in range(4):
        if T[i] > 0:
            T[i] -= 1
            num = count
            if i == 0:
                num += A[depth]
            elif i == 1:
                num -= A[depth]
            elif i == 2:
                num *= A[depth]
            else:
                if num < 0:
                    num = abs(num) // abs(A[depth])
                    num = -num
                else:
                    num = num // A[depth]
            dfs(depth+1, num, N)
            T[i] += 1


dfs(1, A[0], N)

print(max_answer)
print(min_answer)
