# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        now = 0
        higher = 0
        for i in gain:
            now += i
            higher = max(higher, now)
        return higher
