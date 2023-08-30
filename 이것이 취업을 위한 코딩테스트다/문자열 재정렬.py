import sys
input = sys.stdin.readline

S = list(input().rstrip("\n"))
result = ""
count = 0
for i in S:
    if i.isalpha():
        result += i
    else:
        count += int(i)

answer = "".join(sorted(result))
print(answer+str(count))
