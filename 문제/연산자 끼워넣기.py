import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
cal = list(map(int, input().split()))


def calc_num(num, deps, c):
    if(c == 0):
        num += numbers[deps]
    elif(c == 1):
        num -= numbers[deps]
    elif(c == 2):
        num *= numbers[deps]
    elif(c == 3):
        if(num < 0):
            num = abs(num) // abs(numbers[deps])
            num = -num
        else:
            num = num // numbers[deps]
    return num


def find_max(count, deps):
    global max_result
    global N
    flag = False
    if(deps > N):
        max_result = max(max_result, count)
        return
    for i in range(4):
        if(cal[i] != 0):
            flag = True
    if(not flag):
        max_result = max(max_result, count)
        return
    for i in range(4):
        if cal[i] != 0:
            cal[i] -= 1
            result = calc_num(count, deps, i)
            find_max(result, deps+1)
            cal[i] += 1


def find_min(count, deps):
    global min_result
    global N
    if(deps > N):
        min_result = min(min_result, count)
        return
    flag = False
    for i in range(4):
        if(cal[i] != 0):
            flag = True
    if(not flag):
        min_result = min(min_result, count)
        return
    for i in range(4):
        if cal[i] > 0:
            cal[i] -= 1
            result = calc_num(count, deps, i)
            find_min(result, deps+1)
            cal[i] += 1


max_result =-10000000000000000
min_result = 10000000000000000

find_max(numbers[0], 1)
find_min(numbers[0], 1)

print(max_result)
print(min_result)
