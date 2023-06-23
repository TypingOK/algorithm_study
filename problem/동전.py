import sys

input = sys.stdin.readline
N = input().rstrip("\n")
stack = []
for i in N:
    stack.append(i)
    if len(stack) >= 4:
        if "PPAP" == "".join(stack[-4:]):
            for _ in range(3):
                stack.pop()

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")
