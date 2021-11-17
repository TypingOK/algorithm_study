#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
#입력 -> [1,4,3,2]
#출력 -> 4

def solution(n):
    n.sort()
    sum=0
    for i,idx in enumerate(n):
        if i%2==0:
            sum+=idx
    return sum
    

n=[1,4,3,2]
print(solution(n))