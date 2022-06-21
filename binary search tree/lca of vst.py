# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        mx, mn = max(p.val, q.val), min(p.val, q.val)
        while root:
            if root.val > mx:
                root = root.left
            elif root.val < mn:
                root = root.right
            else:
                return root
        return None
