# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, sums, k):
        if not node:
            return
        if sums + node.val == k:
            self.ans += 1
        self.dfs(node.left, sums + node.val, k)
        self.dfs(node.right, sums + node.val, k)

    def solve(self, root, k):
        if not root:
            return
        self.dfs(root, 0, k)
        self.solve(root.left, k)
        self.solve(root.right, k)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.solve(root, targetSum)
        return self.ans
