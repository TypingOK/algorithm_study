
N = int(input())

switch = [0] * N

answer = list(map(int, input().split()))

count = 0
for i in range(N):
    if switch[i] != answer[i]:
        count += 1
        switch[i] = not switch[i]
        if(i+1 < N):
            switch[i+1] = not switch[i+1]
        if(i+2 < N):
            switch[i+2] = not switch[i+2]

print(count)
