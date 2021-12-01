# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    temp = []
    result = ""
    for i in range(1, len(s)//2+2):
        st = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if(s[j:j+i] == st):
                cnt += 1
            else:
                if(cnt == 1):
                    cnt = ""
                result += str(cnt)+st
                st = s[j:j+i]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt)+st
        temp.append(len(result))
        result = ""
    return min(temp)
