import sys
input = sys.stdin.readline
S = input().rstrip("\n")

count_zero = S.count("0") // 2
count_one = S.count("1") // 2

index = 0

count = 0
while count < count_one:
    if S[index] == "1":
        S = S[:index] + S[index+1:]
        count += 1
    else:
        index += 1

count = 0

index = len(S) - 1

while count < count_zero:
    if S[index] == "0":
        S = S[:index] + S[index + 1:]
        count += 1

    index -= 1

print(S)
