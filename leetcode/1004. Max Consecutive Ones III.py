# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maximum = 0
        count = k
        while right < len(nums):
            if nums[right] == 0:
                count -= 1
            while count < 0:
                if nums[left] == 0:
                    count += 1
                left += 1
            right += 1
            maximum = max(maximum, right - left)
        return maximum
