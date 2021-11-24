N=int(input())
student=[]
for i in range(N):
    a,b=input().split()
    student.append((a,int(b)))

# def data(student):
#     return student[1]
answer=sorted(student, key = lambda student:student[1])
for j in answer:
    print(j[0],end=' ')