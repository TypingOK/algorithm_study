import sys
input = sys.stdin.readline

S = input().rstrip("\n")
i = 1

while True:
    num = str(i)
    while len(num) > 0 and len(S) > 0:
        if num[0] == S[0]:
            S = S[1:]

        num = num[1:]

    if S == "":
        print(i)
        break
    i += 1
