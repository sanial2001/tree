# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, k):
        if not node:
            return
        left = self.solve(node.left, k)
        right = self.solve(node.right, k)
        if not left and not right and node.val == k:
            return None
        node.left, node.right = left, right
        return node

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.solve(root, target)
