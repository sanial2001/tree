# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p, q):
        if not node:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        l, r = self.dfs(node.left, p, q), self.dfs(node.right, p, q)
        if l and r:
            return node
        if l:
            return l
        if r:
            return r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
