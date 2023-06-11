import sys

input = sys.stdin.readline


def find(x):
    if x != root[x]:
        root[x] = find(root[x])

    return root[x]


def union(x, y):
    nx = find(x)
    ny = find(y)

    if nx in know and ny in know:
        return

    if nx in know:
        root[ny] = nx
    elif ny in know:
        root[nx] = ny
    else:
        if nx > ny:
            root[nx] = ny
        else:
            root[ny] = nx


N, M = map(int, input().split())
temp_know = list(map(int, input().split()))

know = temp_know[1:]
root = [i for i in range(N+1)]
parties = []

for i in range(M):
    temp = list(map(int, input().split()))
    len_party = temp[0]
    party = temp[1:]

    for i in range(len_party-1):
        union(party[i], party[i+1])
    parties.append(party)

count = 0

for i in parties:
    for j in range(len(i)):
        if find(i[j]) in know:
            break
    else:
        count += 1
print(count)
