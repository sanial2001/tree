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
        self.dfs(node.right)
        self.sum += node.val
        node.val = self.sum
        self.dfs(node.left)
        return node

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        return self.dfs(root)
