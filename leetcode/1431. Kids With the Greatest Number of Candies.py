# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)

        return result
