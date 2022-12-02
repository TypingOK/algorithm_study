L, R = map(str, input().split())

count = 0
if(len(L) < len(R)):
    print(0)
else:
    for i in range(len(R)):
        if L[i] == R[i]:
            if L[i] == '8':
                count += 1
        else:
            break
    print(count)
