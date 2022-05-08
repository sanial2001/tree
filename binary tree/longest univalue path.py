# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left, right = self.dfs(node.left), self.dfs(node.right)
        left_st = left + 1 if node.left and node.val == node.left.val else 0
        right_st = right + 1 if node.right and node.val == node.right.val else 0
        self.ans = max(self.ans, left_st + right_st)
        return max(left_st, right_st)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
