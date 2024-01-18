# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k-1
        count = 0
        for i in range(k):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                count += 1
        answer = count
        left += 1
        right += 1

        while right < len(s):
            if s[left-1] == "a" or s[left-1] == "e" or s[left-1] == "i" or s[left-1] == "o" or s[left-1] == "u":
                count -= 1
            if s[right] == "a" or s[right] == "e" or s[right] == "i" or s[right] == "o" or s[right] == "u":
                count += 1
            answer = max(count, answer)
            left += 1
            right += 1
        return answer
