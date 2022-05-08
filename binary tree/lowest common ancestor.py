# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, path, p):
        if not node:
            return
        if node.val == p.val:
            path.append(node)
            self.path = path
            return
        self.dfs(node.left, path + [node], p)
        self.dfs(node.right, path + [node], p)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path = []
        self.dfs(root, [], p)
        x = self.path[::]
        self.dfs(root, [], q)
        y = self.path[::]
        n = min(len(x), len(y))
        ans = None
        i = 0
        while i < n:
            if x[i].val == y[i].val:
                ans = x[i]
            else:
                break
            i = i + 1
        return ans
