import sys

N = int(sys.stdin.readline())

number = [int(sys.stdin.readline()) for i in range(N)]

number.sort(reverse=True)

for i in number:
    print(i)
