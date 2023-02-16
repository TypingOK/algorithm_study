import sys
input = sys.stdin.readline

N, K = map(int, input().split())


def dfs(idx, depth):
    global answer

    if idx == K-5:
        count = 0

        for i in words:
            flag = True
            for j in i:
                if not alpha[ord(j) - ord('a')]:
                    flag = False
                    break
            if flag:
                count += 1
        answer = max(answer, count)
        return

    for i in range(depth, 26):
        if (alpha[i] == False):
            alpha[i] = True
            dfs(idx+1, i)
            alpha[i] = False


if (K < 5):
    print(0)
    exit()
elif (K >= 26):
    print(N)
    exit()

words = [input().rstrip() for i in range(N)]
alpha = [False] * 26

for i in ('a', 'n', 't', 'i', 'c'):
    alpha[ord(i) - ord('a')] = True

answer = 0
dfs(0, 0)
print(answer)
