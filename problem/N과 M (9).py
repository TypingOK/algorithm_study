import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
selected = []
visited = [False] * N
result = set()


def perm(idx):
    if(idx == M):
        # answer = " ".join(map(str, selected))
        # print(answer)
        result.add(tuple(selected))
        return

    for i in range(N):
        if(not visited[i]):
            selected.append(numbers[i])
            visited[i] = True
            perm(idx+1)
            visited[i] = False
            selected.pop()


numbers.sort()
perm(0)

temp = list(result)
temp.sort()

for i in range(len(temp)):
    answer = " ".join(map(str,temp[i]))
    print(answer)