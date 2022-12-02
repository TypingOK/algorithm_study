N = int(input())
m = list(map(int, input().split()))
m.sort()
result = 0
count = 0

for i in m:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
