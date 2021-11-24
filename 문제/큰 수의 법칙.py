N, M, K = list(map(int, input().split()))
number = list(map(int, input().split()))
index = [0 for _ in range(len(number))]
number.sort(reverse=True)
answer = 0
m = 0
while m < M:
    for i in range(K):
        if m >= M:
            break
        answer += number[0]
        m += 1
    if m < M:
        answer += number[1]
        m += 1
print(answer)


# 반복 되는 수열을 찾아서 결과를 찾는 방법 (시간이 더 절약되기 때문에 훨씬 효율적인 방법)

# 가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
# 첫번째로 큰 수 더해주기
result += count*number[0]
# 두번째로 큰 수 더해주기
result += (m-count) * number[1]
print(result)
