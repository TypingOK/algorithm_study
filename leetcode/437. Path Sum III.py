# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, root, numbers, count, targetSum, index):
        if not root:
            return count
        numbers.append(root.val)
        for i in range(index, len(numbers)):
            result = sum(numbers[i:len(numbers)])
            if result == targetSum:
                # print(result)
                count += 1
                # break
        # print(count,numbers,index)
        count = self.dfs(root.left, numbers, count, targetSum, index)
        count = self.dfs(root.right, numbers, count, targetSum, index)
        numbers.pop()
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.dfs(root, [],0,targetSum,0)