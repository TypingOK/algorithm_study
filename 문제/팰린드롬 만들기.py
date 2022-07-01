import sys

input = sys.stdin.readline

word = input()
temp = []
for i in word:
    temp.append(i)
temp.pop()
temp.sort()

dic = {}
for i in temp:
    if i in dic.keys():
        dic.update({i: dic.get(i)+1})
    else:
        dic[i] = 1

left = []
right = []
center = []
for k, v in dic.items():
    if(v % 2 == 0):
        for i in range(v//2):
            left.append(k)
            right.append(k)
    else:
        for i in range(v//2):
            left.append(k)
            right.append(k)
        center.append(k)

if(len(center)<2 and left.sort() == right.sort()):
    right.sort(reverse=True)
    if(len(center) == 1):
        left.extend(center)
    left.extend(right)
    print("".join(left))
else:
    print("I'm Sorry Hansoo")
