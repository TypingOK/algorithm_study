import sys
input = sys.stdin.readline

N, K = map(int, input().split())
st = list(input())

count = 0
for i in range(len(st)):
    flag = False
    if st[i] == 'P':
        for j in range(K, 0, -1):
            if(i-j >= 0):
                if st[i-j] == 'H':
                    count += 1
                    st[i-j] = '.'
                    flag = True
                    break
        if(not flag):
            for j in range(K+1):
                if(j+i < N):
                    if st[j+i] == 'H':
                        count += 1
                        st[j+i] = '.'
                        break
    # print(st)


print(count)
