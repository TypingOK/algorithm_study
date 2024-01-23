# https://leetcode.com/problems/find-pivot-index/submissions/1154101197/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        right -= nums[0]

        for i in range(len(nums)-1):
            if left == right:
                return i
            left += nums[i]
            right -= nums[i+1]

        if left == right:
            return len(nums)-1
        return -1
