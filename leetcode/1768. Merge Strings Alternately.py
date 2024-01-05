# https://leetcode.com/problems/merge-strings-alternately/?source=submission-ac
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        index = 0
        while index < len(word1) or index < len(word2):
            if index < len(word1):
                result += word1[index]
            if index < len(word2):
                result += word2[index]
            index += 1

        return result
# 문자열을 번갈아가면서 더해주기만 하면 된다.
# 하나가 끝났다면 다른 녀석을 그냥 더해주기만 해주면 된다.