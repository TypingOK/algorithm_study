S = input()
T = input()


def check(T):
    if len(S) == len(T):
        if(S == T):
            return True
        else:
            return False
    if T[0] == "B" and check(T[:0:-1]):
        return True
    if T[-1] == "A" and check(T[0:-1]):
        return True


if(check(T)):
    print(1)

else:
    print(0)
