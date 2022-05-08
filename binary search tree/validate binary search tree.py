# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        left = self.check(node.left, low, node.val)
        right = self.check(node.right, node.val, high)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, float("-inf"), float("inf"))
