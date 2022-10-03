# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, node):
        while node.left:
            node = node.left
        return node

    def solve(self, node, key):
        if not node:
            return None
        if node.val < key:
            node.right = self.solve(node.right, key)
        elif node.val > key:
            node.left = self.solve(node.left, key)
        elif node.val == key:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                mn = self.find(node.right)
                # print(mn.val)
                node.val = mn.val
                node.right = self.solve(node.right, node.val)
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.solve(root, key)
