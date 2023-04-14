import sys

input = sys.stdin.readline

temp = list(input().rstrip())

result = []
for i in temp:
    if 'A' <= i[0] <= "Z":
        result.append(i[0])
result = "".join(result)
u = result.find("U")
c = result.find("C", u)
p = result.find("P", c)
c2 = 0
if c < p:
    c2 = result.find("C", p)
if u < c < p < c2:
    print("I love UCPC")
else:
    print("I hate UCPC")
