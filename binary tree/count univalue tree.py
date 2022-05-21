# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return True
        l, r = self.dfs(node.left), self.dfs(node.right)
        if l == False or r == False:
            return False
        if node.left and node.left.val != node.val:
            return False
        if node.right and node.right.val != node.val:
            return False
        self.ans += 1
        return True

    def solve(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans
