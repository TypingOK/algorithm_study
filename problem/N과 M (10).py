import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
selected = []
visited = [False] * N
temp = set()


def perm(idx):
    if(len(selected) > 1):
        for i in range(1, len(selected)):
            if(selected[i-1] > selected[i]):
                return

    if(idx == M):
        temp_selected = tuple(selected)
        if(temp_selected not in temp):
            temp.add(temp_selected)
            answer = " ".join(map(str, selected))
            print(answer)
        return

    for i in range(N):
        if(not visited[i]):
            visited[i] = True
            selected.append(numbers[i])
            perm(idx+1)
            visited[i] = False
            selected.pop()


perm(0)
