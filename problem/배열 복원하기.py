import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

A = []
B = []
for i in range(H+X):
    temp = list(map(int, input().split()))
    B.append(temp)

for i in range(X):
    temp = []
    for j in range(W):
        temp.append(B[i][j])
    A.append(temp)

for i in range(X, H):
    temp = []
    # if i == X:
    for j in range(0, Y):
        temp.append(B[i][j])
    for j in range(Y, W):
        temp.append(B[i][j] - A[i-X][j-Y])

    A.append(temp)

# print(A)
for i in range(H):
    for j in range(W):
        print(A[i][j], end=" ")
    print()
