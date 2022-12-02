import sys
input = sys.stdin.readline

n = int(input())
word = input()
b = 0
r = 0
for i in range(1, n):
    if(word[i]==word[i-1]):
        continue
    if(word[i-1]=='B'):
        b+=1
    elif(word[i-1]=='R'):
        r+=1
if(word[n-1] == 'B'):
    b+=1
elif(word[n-1]=='R'):
    r+=1

print(min(b, r)+1)
