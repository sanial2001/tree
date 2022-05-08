# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, min_val, max_val):
        if not node:
            return
        min_val, max_val = min(min_val, node.val), max(max_val, node.val)
        self.ans = max(self.ans, max_val - min_val)
        self.dfs(node.left, min_val, max_val)
        self.dfs(node.right, min_val, max_val)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self.dfs(root, float("inf"), float("-inf"))
        return self.ans
