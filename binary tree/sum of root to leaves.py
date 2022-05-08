# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path = path + str(node.val)
            self.ans += int(path, 2)
            return
        self.dfs(node.left, path + str(node.val))
        self.dfs(node.right, path + str(node.val))

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, '')
        return self.ans

