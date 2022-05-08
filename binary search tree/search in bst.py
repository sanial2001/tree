# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        return self.dfs(node.left, val) if val < node.val else self.dfs(node.right, val)

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)
