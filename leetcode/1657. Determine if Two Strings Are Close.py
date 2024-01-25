# https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        sorted_word1 = sorted(word1)
        sorted_word2 = sorted(word2)
        if set(sorted_word1) != set(sorted_word2):
            return False
        dic_word1 = {}
        dic_word2 = {}
        for i in sorted_word1:
            if i in dic_word1:
                dic_word1[i] += 1
            else:
                dic_word1[i] = 1

        for i in sorted_word2:
            if i in dic_word2:
                dic_word2[i] += 1
            else:
                dic_word2[i] = 1
        count_word1 = list(dic_word1.values())
        count_word2 = list(dic_word2.values())
        count_word1.sort()
        count_word2.sort()

        if count_word1 == count_word2:
            return True
        else:
            return False
