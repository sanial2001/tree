# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, parent):
        if not node:
            return [0, 0]
        l, r = self.dfs(node.left, node), self.dfs(node.right, node)
        self.ans = max(self.ans, l[0] + r[1] + 1, l[1] + r[0] + 1)
        if parent and node.val + 1 == parent.val:
            return [max(l[0], r[0]) + 1, 0]
        if parent and node.val - 1 == parent.val:
            return [0, max(l[1], r[1]) + 1]
        return [0, 0]

    def solve(self, root):
        self.ans = 0
        self.dfs(root, None)
        return self.ans
