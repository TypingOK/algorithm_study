# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        answer = 0
        if nums.count(0) == 0:
            return len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == 0:
                while zeros > 0:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
                zeros += 1
            answer = max(answer, i - left)
        return answer
