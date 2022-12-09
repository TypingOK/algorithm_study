import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
selected = []
temp = set()


def perm(idx):
    if(idx == M):
        temp_selected = tuple(selected)
        if(temp_selected not in temp):
            temp.add(temp_selected)
            answer = " ".join(map(str, selected))
            print(answer)
        return

    for i in range(N):

        selected.append(numbers[i])
        perm(idx+1)

        selected.pop()


perm(0)
