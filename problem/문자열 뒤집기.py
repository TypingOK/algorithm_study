import sys

N=input()
one=0
zero=0


for i in range(len(N)-1):
    if N[i]!=N[i+1] and N[i]=='1':
        one+=1
    elif N[i] != N[i+1] and N[i] == '0':
        zero+=1
if N[-1]=='0':
    zero+=1
elif N[-1]=='1':
    one+=1
if one<zero:
    print(one)
else:
    print(zero)
