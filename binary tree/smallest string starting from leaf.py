# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 'z' * 13
        self.m = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path = self.m[node.val] + path
            self.ans = min(self.ans, path)
            return
        self.dfs(node.left, self.m[node.val] + path)
        self.dfs(node.right, self.m[node.val] + path)

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.dfs(root, '')
        return self.ans
