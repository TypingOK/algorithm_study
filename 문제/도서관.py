import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

book = list(map(int, input().split(" ")))

positive = []
negative = []
maxVal = 0
for i in book:
    if i > 0:
        positive.append(i)
    else:
        negative.append(abs(i))
    if maxVal < abs(i):
        maxVal = abs(i)

positive.sort(reverse=True)
negative.sort(reverse=True)

# maxVal = max(positive[0], negative[0])

dist = []
for i in range(0, len(positive), m):
    if(positive[i] != maxVal):
        dist.append(positive[i])
for i in range(0, len(negative), m):
    if(negative[i] != maxVal):
        dist.append(negative[i])
count = maxVal

for i in dist:
    count += (i*2)
print(count)
