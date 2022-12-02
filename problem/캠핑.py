index = 1
while(True):
    L,P,V = map(int,input().split())

    answer =0
    if(L==0 and P == 0 and V ==0 ):
        break
    while(True):
        if V // P >0:
            answer += (L * (V//P))
            V = V%P
        elif V<=P and V>=L:
            answer += L
            break
        else:
            answer += (V%L)
            break
    print("Case "+ str(index)+": "+str(answer))
    index=1+index
