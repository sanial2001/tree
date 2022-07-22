# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, sums):
        if not node:
            return
        if not node.left and not node.right:
            path += 1
            sums += node.val
            print(path, sums)
            if path > self.long_path:
                self.long_path = path
                self.ans = sums
            elif path == self.long_path:
                self.ans = max(self.ans, sums)
            return
        self.dfs(node.left, path + 1, sums + node.val)
        self.dfs(node.right, path + 1, sums + node.val)

    def solve(self, root):
        self.ans = 0
        self.long_path = 0
        self.dfs(root, 0, 0)
        return self.ans
