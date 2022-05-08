# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [-1, -1]
        l_l, l_r = self.dfs(node.left)
        r_l, r_r = self.dfs(node.right)
        max_root = 1 + max(l_r, r_l)
        self.ans = max(self.ans, max_root)
        return [1 + l_r, 1 + r_l]

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
