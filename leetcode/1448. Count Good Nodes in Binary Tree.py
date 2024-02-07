# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, count: int, max_val: int, root: TreeNode):
        if not root:
            return count
        if max_val <= root.val:
            count += 1
            max_val = root.val
        count = self.dfs(count, max_val, root.left)
        count = self.dfs(count, max_val, root.right)
        return count

    def goodNodes(self, root: TreeNode) -> int:
        count = self.dfs(0, root.val, root)
        return count
