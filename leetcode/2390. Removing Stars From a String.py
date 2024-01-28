# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        temp = []
        for i in s:
            if i != '*':
                temp.append(i)
            else:
                temp.pop()

        return "".join(temp)
