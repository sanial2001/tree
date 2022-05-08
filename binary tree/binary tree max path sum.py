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
        mst = max(node.val, max(left, right) + node.val)
        msp = max(mst, left + right + node.val)
        self.ans = max(msp, self.ans)
        return mst

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -100000
        self.dfs(root)
        return self.ans
