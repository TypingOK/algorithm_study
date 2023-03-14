import sys

input = sys.stdin.readline

N = int(input())
egg = []

for i in range(N):
    egg.append(list(map(int, input().split())))

answer = 0
crack = [False] * N


def solution(depth, count, grap):
    global answer
    # print("depth", depth, "count : ", count)
    if grap == N or depth == N:
        answer = max(answer, count)
        return
    if crack[grap]:
        solution(depth+1, count, grap+1)
        return
    flag = False
    for i in range(N):
        if i != grap and not crack[i]:
            flag = True
            temp = egg[grap][0] - egg[i][1]
            temp2 = egg[i][0] - egg[grap][1]
            if (temp <= 0 and temp2 <= 0):
                crack[i] = True
                crack[grap] = True
                solution(depth+1, count+2, grap+1)
                crack[i] = False
                crack[grap] = False
            elif (temp <= 0 and temp2 > 0):
                crack[grap] = True
                temp3 = egg[i][0]
                egg[i][0] = temp2
                solution(depth+1, count+1, grap+1)
                egg[i][0] = temp3
                crack[grap] = False
            elif (temp > 0 and temp2 <= 0):
                crack[i] = True
                temp3 = egg[grap][0]
                egg[grap][0] = temp
                solution(depth+1, count+1, grap+1)
                crack[i] = False
                egg[grap][0] = temp3
            else:
                temp3 = egg[grap][0]
                temp4 = egg[i][0]
                egg[grap][0] = temp
                egg[i][0] = temp2
                solution(depth+1, count, grap+1)
                egg[grap][0] = temp3
                egg[i][0] = temp4
    if (not flag):
        solution(N, count, grap)


solution(0, 0, 0)
print(answer)
