import sys
input = sys.stdin.readline

N, M = map(int, input().split())

c = []
for i in range(N):
    p, k = map(int, input().split())
    students = list(map(int, input().split()))

    if len(students) < k:
        c.append(1)
    else:
        students.sort(reverse=True)
        c.append(students[k-1])

c.sort()
answer = 0
for mile in c:
    if M - mile >= 0:
        answer += 1
        M -= mile
print(answer)
