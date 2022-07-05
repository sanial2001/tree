# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, depth):
        if not node:
            return
        if not node.left and not node.right:
            if depth not in self.ht:
                self.ht.append(depth)
            return
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def solve(self, root):
        self.ht = []
        self.dfs(root, 0)
        self.ht.sort()
        return self.ht[-2]
