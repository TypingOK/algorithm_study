# n=list(input())
# n.sort()

# num=['0','1','2','3','4','5','6','7','8','9']
# indexTemp=0
# for i in range(len(n)):
#     if n[i] not in num:
#         indexTemp=i
#         break

# number=map(int,n[:indexTemp])
# for i in range(indexTemp):
#     n.pop(0)
# n+=str(sum(number))
# print(''.join(n))

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
