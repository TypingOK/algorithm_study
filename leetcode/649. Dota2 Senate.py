# https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rad = deque()
        dir = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dir.append(i)

        while rad and dir:
            r = rad.popleft()
            d = dir.popleft()

            if r < d:
                rad.append(n+r)
            else:
                dir.append(n+d)

        if rad:
            return "Radiant"
        else:
            return "Dire"
