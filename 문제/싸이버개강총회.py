import sys
input = sys.stdin.readline

answer = 0

time = list(input().split())

start = int(time[0][:2]+time[0][3:])
endStart = int(time[1][:2]+time[1][3:])
end = int(time[2][:2]+time[2][3:])

student = {}
chat = []

for i in sys.stdin:
    live = list(i.split())

    enter = int(live[0][:2]+live[0][3:])
    name = live[1]
    if(enter <= start):
        student[name] = enter
    else:
        if(enter >= endStart and enter <= end):
            if (name in student) and (name not in chat):
                answer += 1
                chat.append(name)
# print(student)
print(answer)
