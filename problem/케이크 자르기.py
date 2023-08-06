import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
spot = []

for i in range(M):
    spot.append(int(input()))
spot.append(L)
counts = []
for i in range(N):
    counts.append(int(input()))


def binary_search(start, end, cut_count):
    result = 0
    while (start <= end):
        mid = (start+end)//2
        cut = 0
        now = 0
        for i in spot:
            if i - now >= mid:
                cut += 1
                now = i
        if cut > cut_count:
            start = mid + 1
            result = max(mid, result)
        else:
            end = mid - 1
    return result


for cur in range(N):
    result = binary_search(1, L, counts[cur])
    print(result)
