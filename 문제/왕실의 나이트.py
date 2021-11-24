data=input()
row=int(data[1])
chess_index=['a','b','c','d','e','f','g','h']
col=int(chess_index.index(data[0]))+1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
result=0
for step in steps:
    nx=row+step[0]
    ny=col+step[1]
    if nx>=1 and ny<=8 and ny>=1 and nx<=8 :
        result+=1
print(result)