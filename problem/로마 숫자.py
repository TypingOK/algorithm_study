
nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
extra = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def to_num(S):
    chk = [0] * len(S)
    tot = 0
    for i in range(len(S)):
        if not chk[i]:
            if i+1 < len(S) and S[i:i+2] in extra:
                tmp = S[i:i+2]
                tot += extra[tmp]
                chk[i:i+1] = 1, 1
            else:
                tot += nums[S[i]]
                chk[i] = 1
    return tot


def to_str(N):
    ans = ''
    t, n = len(N), len(N)
    while n:
        num = int(N[t-n])
        if n == 4:
            ans += 'M'*num
        elif n == 3:
            if num == 9:
                ans += 'CM'
            elif num == 4:
                ans += 'CD'
            else:
                if num >= 5:
                    ans += 'D'
                ans += 'C'*(num % 5)
        elif n == 2:
            if num == 9:
                ans += 'XC'
            elif num == 4:
                ans += 'XL'
            else:
                if num >= 5:
                    ans += 'L'
                ans += 'X'*(num % 5)
        elif n == 1:
            if num == 9:
                ans += 'IX'
            elif num == 4:
                ans += 'IV'
            else:
                if num >= 5:
                    ans += 'V'
                ans += 'I'*(num % 5)
        n -= 1
    return ans


A, B = input(), input()
a = to_num(A)
b = to_num(B)
total = a + b
print(total)
print(to_str(str(total)))
