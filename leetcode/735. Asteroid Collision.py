# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        temp = []
        for i in a:
            if temp and temp[-1] > 0 and i < 0:
                if temp[-1] > abs(i):
                    continue
                elif temp[-1] == abs(i):
                    temp.pop()
                else:
                    while (temp):
                        if temp[-1] > 0 and temp[-1] < abs(i):
                            temp.pop()
                            if not temp:
                                temp.append(i)
                                break
                        elif temp[-1] > 0 and temp[-1] == abs(i):
                            temp.pop()
                            break
                        else:
                            if temp[-1] < 0 and temp[-1] < abs(i):
                                temp.append(i)
                            break
            else:
                temp.append(i)
        return temp
