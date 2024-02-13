# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], dir: int, count: int) -> int:
        if not root:
            return count
        # 0 == left, 1 == right
        if dir == 0:
            right = self.dfs(root.right, 1, count+1)
            left = self.dfs(root.left, 0, 0)
            return max(left, right)
        if dir == 1:
            left = self.dfs(root.left, 0, count+1)
            right = self.dfs(root.right, 1, 0)
            return max(left, right)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        left = self.dfs(root.left, 0, 0)
        right = self.dfs(root.right, 1, 0)
        return max(left, right)