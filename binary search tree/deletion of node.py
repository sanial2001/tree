# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self, node):
        if not node.right:
            return node
        return self.pre(node.right)

    def solve(self, node, k):
        if not node:
            return None
        if node.val == k:
            if not node.left and not node.right:
                return None
            if node.left and not node.right:
                return node.left
            if node.right and not node.left:
                return node.right
            if node.left and node.right:
                pre = self.pre(node.left)
                node.val = pre.val
                node.left = self.solve(node.left, pre.val)
        if k < node.val:
            return self.solve(node.left, k)
        if k > node.val:
            return self.solve(node.right, k)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.solve(root, k)