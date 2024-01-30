#https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        temp = []
        for i in s:
            if i != ']':
                temp.append(i)
            else:
                st = []
                for j in range(len(temp)-1,-1,-1):
                    if temp[-1].isalpha():
                        st.append(temp[-1])
                        temp.pop()
                    elif temp[-1].isdigit():
                        number = ""
                        for k in range(len(temp)-1,-1,-1):
                            if temp[-1].isdigit():
                                number += temp[-1]
                                temp.pop()
                            else:
                                break
                        reverse_number = number[::-1]
                        reverse_st = "".join(st[::-1])
                        result = ""
                        for _ in range(int(reverse_number)):
                            result += reverse_st
                        temp.append(result)
                        break
                    else:
                        temp.pop()
        return "".join(temp)
