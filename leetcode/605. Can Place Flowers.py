# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        if len(flowerbed) > 1:

            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
            for i in range(len(flowerbed)):
                if (i < len(flowerbed)-1 and flowerbed[i+1] == 0) and (i > 0 and flowerbed[i-1] == 0) and flowerbed[i] == 0:
                    count += 1
                    flowerbed[i] = 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                count += 1
                flowerbed[0] = 1
        else:
            if flowerbed[0] == 0:
                count += 1
        return count >= n
