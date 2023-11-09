import sys
test = ["+", "-", " "]
test.sort()
input = sys.stdin.readline

def re(depth: int, select: str):
    if depth == N+1:
        temp = select.replace(" ", "")
        plus = [i for i, char in enumerate(temp) if char == "+" or char == "-"]
        start = 0
        temp_numbers = []
        for i in plus:
            temp_numbers.append(int(temp[start:i]))
            start = i+1
        temp_numbers.append(int(temp[start:]))
        if len(temp_numbers) > 0:
            count = temp_numbers[0]
            index = 1
            for i in plus:
                if temp[i] == "+":
                    count += temp_numbers[index]
                else:
                    count -= temp_numbers[index]
                index += 1
            if count == 0:
                print(select)
        return
    re(depth+1, select+" "+str(depth))
    re(depth+1, select+"+"+str(depth))
    re(depth+1, select+"-"+str(depth))


T = int(input())
for _ in range(T):
    N = int(input())
    numbers = [i for i in range(1, N+1)]
    re(2, "1")
    print(" ")
