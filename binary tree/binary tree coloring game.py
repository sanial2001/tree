# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def first(self, node, x):
        if not node:
            return
        if node.val == x:
            self.player1 = node
            return
        self.first(node.left, x)
        self.first(node.right, x)

    def count(self, node):
        if not node:
            return 0
        return self.count(node.left) + self.count(node.right) + 1

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.player1 = None
        self.first(root, x)
        first = self.player1
        l = self.count(first.left)
        r = self.count(first.right)
        p = n - (l + r + 1)
        return l > n // 2 or r > n // 2 or p > n // 2
