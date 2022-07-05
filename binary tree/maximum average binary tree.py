# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [0, 0]
        if not node.left and not node.right:
            self.ans = max(self.ans, node.val)
            return [node.val, 1]
        l, r = self.dfs(node.left), self.dfs(node.right)
        self.ans = max(self.ans, (l[0] + r[0] + node.val) / (l[1] + r[1] + 1))
        return [l[0] + r[0] + node.val, l[1] + r[1] + 1]

    def solve(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans
