# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        index = []
        words = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
                index.append(i)
                words.append(s[i])
        words.reverse()
        for i in range(len(index)):
            s[index[i]] = words[i]

        return "".join(s)
