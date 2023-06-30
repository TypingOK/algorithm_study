import sys
input = sys.stdin.readline

temp = list(input().rstrip("\n"))
code = [0]
code += temp

if code[1] == '0':
    print(0)
else:
    dp = [0 for i in range(len(code))]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(code)):
        a = int(code[i])
        b = int(code[i-1]) * 10 + int(code[i])

        if a != 0:
            dp[i] += dp[i-1]
        if 10 <= b <= 26:
            dp[i] += dp[i-2]
    print(dp[len(code)-1] % 1000000)
