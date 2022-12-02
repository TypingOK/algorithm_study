import sys


def solution(n):
    min_s = sys.maxsize
    max_s = 0
    for i in n:
        min_s = min(i, min_s)
        max_s = max(max_s, i-min_s)
    return max_s


n = [2, 4, 1]
print(solution(n))
