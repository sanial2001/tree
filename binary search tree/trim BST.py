# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, i, j):
        if not node:
            return None
        if node.val < i:
            return self.dfs(node.right, i, j)
        if node.val > j:
            return self.dfs(node.left, i, j)
        else:
            node.left, node.right = self.dfs(node.left, i, j), self.dfs(node.right, i, j)
            return node

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.dfs(root, low, high)
