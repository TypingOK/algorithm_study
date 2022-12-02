import sys
input = sys.stdin.readline

N = int(input())
studentNum = int(input())

vote = list(map(int, input().split(" ")))

student = {}
count = 0
index = 0
for i in vote:
    if i in student:
        student[i][0] += 1
    else:
        if count >= N:
            student = dict(
                sorted(student.items(), key=lambda x: (x[1][0], x[1][1])))
            temp = list(student.keys())
            student.pop(temp[0])
        student[i] = [1, index]
        index += 1
        count += 1
answer = sorted(list(student.keys()))
for i in answer:
    print(i, end=" ")
