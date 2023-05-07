import sys
input = sys.stdin.readline

N = int(input())
M, K = map(int, input().split())
pen = list(map(int, input().split()))

people = M * K
if people > sum(pen):
    print("STRESS")
else:
    pen.sort(reverse=True)
    count = 0
    for i in pen:
        people -= i
        count += 1
        if people <= 0:
            break
    print(count)
