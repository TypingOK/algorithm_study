import sys

input = sys.stdin.readline
N = int(input())
weight = list(map(int, input().split(" ")))
M = int(input())
box = list(map(int, input().split(" ")))

weight.sort(reverse=True)
box.sort(reverse=True)

if(box[0] > weight[0]):
    print(-1)
    sys.exit()

answer = 0

while(len(box) > 0):
    index = 0
    for i in weight:
        for j in range(index, len(box)):
            if(len(box) == 0):
                break
            if(i >= box[j]):
                box.pop(j)
                index = j
                break
        if(len(box) == 0):
            break
    answer += 1

print(answer)
