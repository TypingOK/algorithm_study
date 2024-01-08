# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = list(s.split(" "))
        s_filter = [x for x in s_split if x not in " "]

        return " ".join(s_filter)
