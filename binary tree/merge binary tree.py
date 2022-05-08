# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, node1, node2):
        if not node1:
            return node2
        elif not node2:
            return node1
        else:
            root = TreeNode(node1.val + node2.val)
            root.left = self.construct(node1.left, node2.left)
            root.right = self.construct(node1.right, node2.right)
        return root

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.construct(root1, root2)
