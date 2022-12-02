import sys

input = sys.stdin.readline


N = int(input())


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x-i:
            return False
    return True


def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if(check(x)):
                dfs(x+1)


result = 0
row = [0] * N
dfs(0)

print(result)
