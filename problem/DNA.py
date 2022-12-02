import sys

input = sys.stdin.readline

N, M = map(int, input().split(" "))

temp = []

for i in range(N):
    temp.append(input())

count, hap = 0, 0
result = ""

for i in range(M):
    A, C, G, T = 0, 0, 0, 0
    for j in range(N):
        if(temp[j][i] == 'T'):
            T += 1
        elif(temp[j][i] == "G"):
            G += 1
        elif(temp[j][i] == "C"):
            C += 1
        elif(temp[j][i] == "A"):
            A += 1
    if(max(A, C, G, T) == A):
        result += 'A'
        hap += C+G+T
    elif(max(A, C, G, T) == C):
        result += "C"
        hap += A+G+T
    elif(max(A, C, G, T) == G):
        result += "G"
        hap += A+C+T
    elif(max(A, C, G, T) == T):
        result += "T"
        hap += A+G+C

print(result)
print(hap)
