import sys
from itertools import permutations
from copy import deepcopy
INF = 99999999

input = sys.stdin.readline
N, M, K = map(int, input().split())

box = []

for i in range(N):
    temp = list(map(int, input().split()))
    box.append(temp)

rotate = []
for i in range(K):
    temp = list(map(int, input().split()))
    rotate.append(temp)

rotate = list(permutations(rotate, K))

min_count = INF
for i in rotate:
    copy_box = deepcopy(box)
    for j in i:
        top_left_x = j[0] - j[2]-1
        top_left_y = j[1] - j[2]-1
        bottom_right_x = j[0] + j[2]-1
        bottom_right_y = j[1]+j[2]-1
        length_x = bottom_right_x - top_left_x+1
        length_y = bottom_right_y - top_left_y+1
        cur = min(length_x, length_y)
        for k in range(cur//2):
            temp = copy_box[top_left_x+k][top_left_y+k]
            for n in range(top_left_x+k, bottom_right_x-k):
                copy_box[n][top_left_y+k] = copy_box[n+1][top_left_y+k]
            for n in range(top_left_y+k, bottom_right_y-k):
                copy_box[bottom_right_x-k][n] = copy_box[bottom_right_x-k][n+1]
            for n in range(bottom_right_x-k, top_left_x+k, -1):
                copy_box[n][bottom_right_y-k] = copy_box[n-1][bottom_right_y-k]
            for n in range(bottom_right_y-k, top_left_y+k, -1):
                copy_box[top_left_x+k][n] = copy_box[top_left_x+k][n-1]
            copy_box[top_left_x+k][top_left_y+k+1] = temp
    for k in copy_box:
        min_count = min(min_count, sum(k))
print(min_count)
