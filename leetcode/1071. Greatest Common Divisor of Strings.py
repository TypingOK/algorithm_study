# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ""
        for i in range(1, min(len(str1), len(str2))+1):
            flag1 = False
            flag2 = False
            temp_str1 = str1
            temp_str2 = str2
            while temp_str1:
                if temp_str1[:i] == str2[:i]:
                    temp_str1 = temp_str1[i:]
                else:
                    flag1 = True
                    break
            while temp_str2:
                if temp_str2[:i] == str2[:i]:
                    temp_str2 = temp_str2[i:]
                else:
                    flag1 = True
                    break
            if flag1 == False and flag2 == False:
                answer = str1[:i]

        return answer

# 문자열을 잘라내고 서로 같은 문자열인지 확인하고 맞다면 잘라내면서 끝까지 같은 문자열로 잘라낼 수 있는지 확인