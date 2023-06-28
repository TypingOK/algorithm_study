import sys

input = sys.stdin.readline
# 1.수평으로 두칸 이동, 수직으로 한칸
# 2.수직으로 두칸 이동, 수평으로 한칸
dx = [-1, 1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

night = input().rstrip("\n")
y = ord(night[0]) - ord('a')
x = int(night[1]) - 1

answer = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1

print(answer)
