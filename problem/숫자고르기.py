import sys
input = sys.stdin.readline

N = int(input())

number = [0]
for _ in range(N):
    number.append(int(input()))
answer = set()


def dfs(first, second, num):
    first.add(num)
    second.add(number[num])

    if number[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    return dfs(first, second, number[num])


for i in range(1, N+1):
    if i not in answer:
        dfs(set(), set(), i)

print(len(answer))
answer_list = sorted(list(answer))
for i in answer_list:
    print(i)
