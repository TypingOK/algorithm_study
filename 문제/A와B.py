import sys

# input = sys.stdin.readline
sys.setrecursionlimit(1000000)

S = input()
T = input()


def check(T):
    if len(T) == len(S):

        if T == S:
            return True
        else:
            return False

    if(T[-1] == 'B' and check(T[-2::-1])):
        return True
    elif(T[-1] == 'A' and check(T[:-1])):
        return True


if(check(T)):
    print(1)
else:
    print(0)
