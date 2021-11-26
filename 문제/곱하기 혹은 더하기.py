N=input()


N=list(N)
answer=int(N[0])
for i in range(1,len(N)):
    if answer==0 or N[i]=='0' or answer=='1' or N[i]=='1':
        answer+=int(N[i]) 
    else:
        answer= answer*int(N[i])
print(answer)