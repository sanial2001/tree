# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return
        if node.val % 2 == 0:
            if node.left:
                if node.left.left:
                    self.ans += node.left.left.val
                if node.left.right:
                    self.ans += node.left.right.val
            if node.right:
                if node.right.left:
                    self.ans += node.right.left.val
                if node.right.right:
                    self.ans += node.right.right.val
        self.dfs(node.left)
        self.dfs(node.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
