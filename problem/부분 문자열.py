import sys

input = sys.stdin.readline
while True:

    line = input().strip()
    if not line:
        break
    S, T = line.split()
    if len(S) > len(T):
        print("No")
    else:
        index = 0
        answer = ""
        for i in T:
            if S[index] == i:
                answer += i
                index += 1
                if len(answer) == len(S):
                    break
        if answer == S:
            print("Yes")
        else:
            print("No")
