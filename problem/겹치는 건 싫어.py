import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
start = 0
end = 1

key = 0
temp = 0
dic = {}
dic[a[start]] = 1
answer = 0


while end < N:
    if start < end and key in dic and dic[key] > K:
        dic[a[start]] -= 1
        start += 1
        continue
    if a[end] in dic:
        dic[a[end]] += 1
        if dic[a[end]] > K:
            key = a[end]
        else:
            answer = max(end-start, answer)
    else:
        dic[a[end]] = 1
        answer = max(end-start, answer)
    
    end += 1

print(answer+1)
