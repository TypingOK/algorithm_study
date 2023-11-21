import sys
input = sys.stdin.readline
N, K = map(int, input().split())

dic = {}
names = []
for i in range(N):
    temp = len(input().rstrip("\n"))
    names.append(temp)

answer = 0
start = 1
end = K+1
for i in range(0, end):
    if names[i] in dic:
        answer += dic[names[i]]
        dic[names[i]] += 1
    else:
        dic[names[i]] = 1
while end < N:
    dic[names[start-1]] -= 1
    if names[end] in dic:
        answer += dic[names[end]]
        dic[names[end]] += 1
    else:
        dic[names[end]] = 1
    start += 1
    end += 1
print(answer)
