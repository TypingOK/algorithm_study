# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        start, end = 0, 0
        if len(chars) == 1:
            return len(chars)
        n = len(chars)
        count = 0
        while start < end or (start < n and end < n):
            while end < n and chars[end] == chars[start]:
                count += 1
                end += 1
            result.append(chars[start])

            if count > 1:
                temp = str(count)
                for i in temp:
                    result.append(i)

            start = end
            count = 0

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)
