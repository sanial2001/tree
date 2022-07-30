# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return [None, True]
        if not node.left and not node.right:
            return [node.val, True]
        l, r = self.dfs(node.left), self.dfs(node.right)
        # print(l ,r)
        if l[1] and r[1] and (l[0] == node.val or l[0] == None) and (r[0] == node.val or r[0] == None):
            return [node.val, True]
        else:
            return [node.val, False]

    def solve(self, root):
        return self.dfs(root)[1]
