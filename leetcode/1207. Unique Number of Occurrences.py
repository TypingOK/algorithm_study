# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict()

        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        nums = list(dic.values())
        if len(nums) == len(set(nums)):
            return True
        else:
            return False
