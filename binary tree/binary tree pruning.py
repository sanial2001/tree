# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [None, 0]
        left, right = self.dfs(node.left), self.dfs(node.right)
        node.left, node.right = left[0], right[0]
        sums = left[1] + right[1] + node.val
        if sums == 0:
            node = None
        return [node, sums]

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[0]
