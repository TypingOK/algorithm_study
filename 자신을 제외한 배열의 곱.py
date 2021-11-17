def solution(n):
    p = 1
    out = []
    for i in range(len(n)):
        out.append(p)
        p = p*n[i]
    p = 1
    for i in range(len(n)-1, 0-1, -1):
        out[i] = out[i]*p
        p = p*n[i]
    return(out)


n = [1, 2, 3, 4]
print(solution(n))
