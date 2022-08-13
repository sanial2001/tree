# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path = str(node.val) + path
            self.ans = min(self.ans, path)
            return
        self.dfs(node.left, str(node.val) + path)
        self.dfs(node.right, str(node.val) + path)

    def solve(self, root):
        self.ans = "z" * 26
        self.dfs(root, "")
        res = [int(val) for val in self.ans]
        return res
