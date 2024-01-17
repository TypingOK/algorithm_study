# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        average = sums/k

        left = 1
        right = k
        while right < len(nums):
            sums -= nums[left-1]
            sums += nums[right]
            average = max(average, sums/k)
            left += 1
            right += 1

        return average
