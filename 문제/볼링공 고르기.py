N, M = map(int, input().split())
data = list(map(int, input().split()))
# 볼링공의 무게는 1~10까지 이므로 11개의 배열을 생성
post = [0]*11

# 각 무게에 해당하는 볼링공의 개수를 카운트
for x in data:
    post[x] += 1

result = 0

for i in range(1, M+1):
    N -= post[i]  # A가 선택할 수 있는 무게가 i인 볼링공의 개수 제외
    result += post[i]*N  # B가 선택하는 경우의 수와 곱하기
print(result)
