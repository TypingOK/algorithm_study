import sys
input = sys.stdin.readline

numbers = list(input().rstrip("\n"))

result = int(numbers[0])
for i in range(1, len(numbers)):
    b = int(numbers[i])

    if (result == 0 or result == 1) or (b == 0 or b == 1):
        result += b
    else:
        result *= b
print(result)
