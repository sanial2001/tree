# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, k, ht):
        if not node:
            return
        if node.left:
            if node.left.val == k:
                self.parent = node.val
                self.ht = ht + 1
                return
        if node.right:
            if node.right.val == k:
                self.parent = node.val
                self.ht = ht + 1
                return
        self.dfs(node.left, k, ht + 1)
        self.dfs(node.right, k, ht + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.ht, self.parent = 0, None
        self.dfs(root, x, 0)
        x_ht = self.ht
        x_par = self.parent
        self.ht, self.parent = 0, None
        self.dfs(root, y, 0)
        y_ht = self.ht
        y_par = self.parent

        return x_ht == y_ht and x_par != y_par
