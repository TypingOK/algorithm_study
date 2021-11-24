N= int(input())
number=[]
for i in range(N):
    number.append(int(input()))
number.sort(reverse=True)
for j in number:
    print(j, end = ' ')
