import sys
input = sys.stdin.readline
N, M = map(str, input().split(" "))


answer = 9999999999999
for i in range(len(M)-len(N)):
    count = 0
    for j in range(len(N)):
        if(N[j] != M[i+j]):
            count += 1
    answer = min(answer, count)

print(answer)
