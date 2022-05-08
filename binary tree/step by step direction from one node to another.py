# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lca(self, node, p, q):
        if not node:
            return None
        if node.val == p or node.val == q:
            return node
        left, right = self.lca(node.left, p, q), self.lca(node.right, p, q)
        if left and right:
            return node
        if left:
            return left
        if right:
            return right

    def dfs(self, node, path, k):
        if not node:
            return
        if node.val == k:
            self.dest_path = path[:]
            return
        self.dfs(node.left, path + "L", k)
        self.dfs(node.right, path + "R", k)

    def ht(self, node, k, h):
        if not node:
            return
        if node.val == k:
            self.start_ht = h
            return
        self.ht(node.left, k, h + 1)
        self.ht(node.right, k, h + 1)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        node = self.lca(root, startValue, destValue)
        self.dest_path, self.start_ht = "", 0
        self.dfs(node, '', destValue)
        self.ht(node, startValue, 0)
        return "U" * self.start_ht + self.dest_path
