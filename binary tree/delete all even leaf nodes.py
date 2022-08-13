# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            if node.val % 2 == 0:
                return None
            else:
                return node
        l, r = self.dfs(node.left), self.dfs(node.right)
        node.left = l
        node.right = r
        if l is None and r is None and node.val % 2 == 0:
            return None
        else:
            return node

    def solve(self, root):
        return self.dfs(root)
