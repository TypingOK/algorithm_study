import sys
input = sys.stdin.readline

N = int(input())


for _ in range(N):
    word = list(input().rstrip("\n"))
    flag = False
    for i in range(1, len(word)):
        if word[-i] > word[-i-1]:
            flag = True
            cur = i
            break

    if not flag:
        print("".join(word))
        continue
    for j in range(cur-1, len(word)):
        if word[j] > word[-cur-1]:
            count = j
    word[-cur-1], word[count] = word[count], word[-cur-1]
    sorted_word = sorted(word[-cur:])
    result = word[0:-cur] + sorted_word
    print("".join(result))
