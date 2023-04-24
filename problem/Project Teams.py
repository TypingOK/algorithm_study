import sys
input = sys.stdin.readline
N = int(input())
student = list(map(int, input().split()))

student.sort()
answer = sys.maxsize
for i in range(N):
    answer = min(answer, student[i]+student[-i-1])
print(answer)
