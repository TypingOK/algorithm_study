import sys
input = sys.stdin.readline
r, c, k = map(int, input().split())
A = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    temp = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = temp[j]

r, c = r-1, c-1

row = 3
col = 3

count = 0
while count <= 100:
    if A[r][c] == k:
        break
    if row >= col:
        temp_col = 0
        for i in range(row):
            temp = {}
            for j in range(col):
                if A[i][j] > 0 and A[i][j] in temp:
                    temp[A[i][j]] += 1
                elif A[i][j] > 0 and A[i][j] not in temp:
                    temp[A[i][j]] = 1

            result = list(temp.items())
            result.sort(key=lambda x: (x[1], x[0]))
            size = len(result) * 2
            if size > 100:
                size = 100
            index = 0
            for j in range(0, size, 2):
                A[i][j] = result[index][0]
                A[i][j+1] = result[index][1]
                index += 1
            for j in range(size, 100):
                A[i][j] = 0
            temp_col = max(size, temp_col)
        col = temp_col

    elif col > row:
        temp_row = 0
        for i in range(col):
            temp = {}
            for j in range(row):
                if A[j][i] != 0 and A[j][i] in temp:
                    temp[A[j][i]] += 1
                elif A[j][i] != 0 and A[j][i] not in temp:
                    temp[A[j][i]] = 1

            result = list(temp.items())
            result.sort(key=lambda x: (x[1], x[0]))
            size = len(result) * 2
            if size > 100:
                size = 100
            index = 0

            for j in range(0, size, 2):
                A[j][i] = result[index][0]
                A[j+1][i] = result[index][1]
                index += 1
            for j in range(size, 100):
                A[j][i] = 0
            temp_row = max(temp_row, size)
        row = temp_row
    count += 1
if count > 100:
    print(-1)
else:
    print(count)
