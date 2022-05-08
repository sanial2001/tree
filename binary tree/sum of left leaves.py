# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, side):
        if not node:
            return
        if not node.left and not node.right:
            if side == "l":
                self.ans += node.val
        self.dfs(node.left, "l")
        self.dfs(node.right, "r")

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, "r")
        return self.ans
