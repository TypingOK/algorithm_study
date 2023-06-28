import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = map(int, input().split())
    money = int(input())

    dp = [0 for _ in range(money+1)]
    dp[0] = 1

    for i in coins:
        for j in range(money+1):
            if j >= i:
                dp[j] += dp[j-i]
    print(dp[money])
