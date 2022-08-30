import sys

input = sys.stdin.readline

N = int(input())

books = []

index = 0
for i in range(N):
    temp = int(input())
    books.append(temp)

index = N
answer = 0
for i in range(N-1, -1, -1):
    if(books[i] != index):
        answer += 1
    else:
        index = index-1
print(answer)
