import sys
input = sys.stdin.readline

N = int(input())
shortcut = set()

answer = []

for _ in range(N):
    temp = list(input().split())
    if (temp[0][0] in shortcut):
        flag = True
        for i in range(len(temp)):
            if temp[i][0] in shortcut:
                continue
            else:
                flag = False
                shortcut.add(temp[i][0].upper())
                shortcut.add(temp[i][0].lower())

                temp[i] = '['+temp[i][0]+']' + temp[i][1:]
                print(" ".join(temp))
                break
        if (flag):
            exit_flag = False
            for i in range(len(temp)):
                if not exit_flag:
                    for j in range(len(temp[i])):
                        if temp[i][j] in shortcut:
                            continue
                        else:
                            shortcut.add(temp[i][j].upper())
                            shortcut.add(temp[i][j].lower())

                            temp[i] = temp[i][0:j] + \
                                '[' + temp[i][j] + ']' + temp[i][j+1:]

                            print(" ".join(temp))
                            exit_flag = True
                            break
                else:
                    break
            if (not exit_flag):
                print(*temp)
    else:
        shortcut.add(temp[0][0].upper())
        shortcut.add(temp[0][0].lower())
        temp[0] = '[' + temp[0][0] + ']' + temp[0][1:]
        print(" ".join(temp))
