import sys
S = list(sys.stdin.readline().rstrip("\n"))
one = 0
zero = 0
if S[0] == "1":
    one += 1
else:
    zero += 1
for i in range(1, len(S)):
    if S[i] == S[i-1]:
        continue
    elif S[i] != S[i-1]:
        if S[i] == "1":
            one += 1
        else:
            zero += 1
if one < zero:
    print(one)
else:
    print(zero)
