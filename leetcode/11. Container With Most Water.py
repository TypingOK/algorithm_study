# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height)-1

        while left < right:
            min_num = min(height[left], height[right])
            water = (right - left) * min_num
            answer = max(water, answer)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return answer
