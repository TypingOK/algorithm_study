N, M = map(int, input().split())

list1 = []
list2 = []

for i in range(M):
    temp = list(map(int, input().split()))
    list1.append(temp[0])
    list2.append(temp[1])
answer = 0
if N <= 6:
    list1.sort()
    list2.sort()

    answer = min(list1[0], list2[0]*N)

else:
    list1.sort()
    list2.sort()
    if(list1[0] != 0):
        temp = N // list1[0]

        if(list1[0] <= (list2[0]*6)):
            answer += ((N//6)*list1[0])
            N = N % 6
            if(answer+list2[0]*N < answer+list1[0]):
                answer += list2[0]*N
            else:
                answer += list1[0]
        else:
            answer = list2[0]*N
    else:
        answer = 0
print(answer)
