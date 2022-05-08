# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return
        self.nums.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.dfs(root)
        min_val = min(self.nums)
        self.nums = [val for val in self.nums if val != min_val]
        return -1 if not self.nums else min(self.nums)
