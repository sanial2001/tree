# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return []
        l, r = self.inorder(node.left), self.inorder(node.right)
        return l + [node.val] + r

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = self.inorder(root)
        return nums[k - 1]
