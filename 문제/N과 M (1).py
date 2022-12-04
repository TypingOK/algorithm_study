import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [i+1 for i in range(N)]

select = [False] * N

pick = []


def perm(idx):
    if idx == M:
        if(len(pick) == M):
            result = " ".join(map(str, pick))
            print(result)
        return
    else:
        for i in range(N):
            if not select[i]:
                pick.append(numbers[i])
                select[i] = True
                perm(idx+1)
                select[i] = False
                pick.pop()


perm(0)
