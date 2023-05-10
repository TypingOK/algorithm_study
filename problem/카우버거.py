import sys
input = sys.stdin.readline

B, C, D = map(int, input().split())

burgur = list(map(int, input().split()))
side = list(map(int, input().split()))
drinks = list(map(int, input().split()))

burgur.sort()
side.sort()
drinks.sort()

sum_answer = sum(burgur) + sum(side) + sum(drinks)
count = 0
while burgur and side and drinks:
    count += int((burgur.pop()+side.pop()+drinks.pop()) * 0.9)

count += sum(burgur) + sum(side) + sum(drinks)

print(sum_answer)
print(count)
