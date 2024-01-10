# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
import sys


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = sys.maxsize
        second = sys.maxsize

        for i in range(len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                return True
        return False
