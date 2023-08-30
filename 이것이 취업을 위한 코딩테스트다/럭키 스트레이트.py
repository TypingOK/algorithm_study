import sys
input = sys.stdin.readline

N = list(input().rstrip("\n"))

mid = len(N)//2
left_count = 0
for i in range(mid):
    left_count += int(N[i])

right_count = 0
for j in range(mid, len(N)):
    right_count += int(N[j])

if left_count == right_count:
    print("LUCKY")
else:
    print("READY")
