import sys

N = int(sys.stdin.readline())

alpha = []
alpha_dict = {}
num_list = []

for i in range(N):
    alpha.append(sys.stdin.readline().rstrip())

for i in range(N):
    for j in range(len(alpha[i])):
        if alpha[i][j] in alpha_dict:
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1)
        else:
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values():
    num_list.append(val)

num_list.sort(reverse=True)

sum = 0
cur = 9

for i in num_list:
    sum += cur * i
    cur -= 1

print(sum)
