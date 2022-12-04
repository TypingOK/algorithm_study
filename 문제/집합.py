import sys

input = sys.stdin.readline

M = int(input())
all_temp = set([i for i in range(1, 21)])
S = set()
for i in range(M):
    n = input().rsplit()
    if(n[0] == "add"):
        S.add(int(n[1]))
    elif(n[0] == "remove"):
        S.discard(int(n[1]))
    elif(n[0] == "check"):
        if(int(n[1]) in S):
            print(1)
        else:
            print(0)
    elif(n[0] == "toggle"):
        try:
            S.remove(int(n[1]))
        except:
            S.add(int(n[1]))
    elif(n[0] == "all"):
        S = all_temp.copy()
    elif(n[0] == "empty"):
        S = set()
