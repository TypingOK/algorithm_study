import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
select = []
temp = set()


def perm(idx):
    if(len(select) > 1):
        for i in range(1, len(select)):
            if(select[i-1] > select[i]):
                return
    if idx == M:
        temp_selected = tuple(select)
        if temp_selected not in temp:
            temp.add(temp_selected)
            answer = " ".join(map(str, temp_selected))
            print(answer)
        return

    for i in range(N):
        select.append(numbers[i])
        perm(idx+1)
        select.pop()


numbers.sort()
perm(0)
