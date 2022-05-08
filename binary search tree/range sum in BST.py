# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, low, high):
        if not node:
            return
        if low <= node.val <= high:
            self.sums += node.val
        if low < node.val:
            self.dfs(node.left, low, high)
        if high > node.val:
            self.dfs(node.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sums = 0
        self.dfs(root, low, high)
        return self.sums
