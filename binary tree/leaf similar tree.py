# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            self.ans.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.ans = []
        self.dfs(root1)
        r1 = self.ans[::]
        self.ans = []
        self.dfs(root2)
        r2 = self.ans[::]
        return r1 == r2
