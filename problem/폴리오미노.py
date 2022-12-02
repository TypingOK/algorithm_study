st = input()

answer = ''
count = 0

if(len(st) == 1 and st[0] == 'X'):
    print(-1)
    exit()
for i in range(len(st)):
    if(st[i] != 'X' and st[i] != '.'):
        print(-1)
        exit()
    if(st[i] == 'X'):
        count += 1
        if(i == len(st)-1):
            if(count % 2 == 1):
                print(-1)
                exit()
            while(count > 0):
                if(count >= 4):
                    answer += 'AAAA'
                    count = count - 4
                else:
                    answer += 'BB'
                    count = count - 2
    else:
        if(count % 2 == 1):
            print(-1)
            exit()
        while(count > 0):
            if(count >= 4):
                answer += 'AAAA'
                count = count - 4
            else:
                answer += 'BB'
                count = count - 2
        count = 0
        answer += '.'

print(answer)