import sys
input = sys.stdin.readline

index = 1
while(True):
    n = input()
    if(n[0] == '-'):
        break
    stack = []
    count = 0
    for i in range(len(n)):
        if(n[i] == '{'):
            stack.append(n[i])
        elif(stack and stack[-1] == '{' and n[i] == '}'):
            stack.pop()
        else:
            stack.append(n[i])
    # print(stack)
    stack.pop()
    if(stack):
        while(stack):
            if(stack[-1] == stack[-2]):

                count += 1
                stack.pop()
                stack.pop()
            else:
                count += 2
                stack.pop()
                stack.pop()
    print(str(index)+". "+str(count))
    index += 1
