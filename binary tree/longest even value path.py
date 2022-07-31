# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        l, r = self.dfs(node.left), self.dfs(node.right)
        if node.val % 2 == 0:
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1
        else:
            return 0

    def solve(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans
