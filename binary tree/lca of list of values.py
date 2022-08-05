# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, values):
        if not node:
            return None
        if node.val in values:
            return node
        l, r = self.dfs(node.left, values), self.dfs(node.right, values)
        if l and r:
            return node
        if l:
            return l
        if r:
            return r

    def solve(self, root, values):
        return self.dfs(root, values)
