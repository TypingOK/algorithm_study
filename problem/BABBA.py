import sys
N = int(sys.stdin.readline())

dp_a = [1 for i in range(46)]
dp_b = [0 for i in range(46)]

dp_a[1] = 0
dp_b[1] = 1
dp_b[2] = 1

for i in range(2, 46):
    dp_a[i] = dp_b[i-1]
    dp_b[i] = dp_b[i-1] + dp_b[i-2]
print(dp_a[N], dp_b[N])
