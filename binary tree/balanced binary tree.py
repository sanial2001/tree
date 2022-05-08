# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [True, 0]
        left, right = self.dfs(node.left), self.dfs(node.right)
        bal = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [bal, 1 + max(left[1], right[1])]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
