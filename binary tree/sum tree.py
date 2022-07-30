# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [0, True]
        if not node.left and not node.right:
            return [node.val, True]
        l, r = self.dfs(node.left), self.dfs(node.right)
        if l[1] and r[1] and l[0] + r[0] == node.val:
            return [node.val, True]
        else:
            return [node.val, False]

    def solve(self, root):
        if not root:
            return True
        return self.dfs(root)[1]
