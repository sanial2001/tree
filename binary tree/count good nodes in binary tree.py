# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, val):
        if not node:
            return
        if node.val >= val:
            self.ans += 1
        self.solve(node.left, max(val, node.val))
        self.solve(node.right, max(val, node.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.solve(root, -100000)
        return self.ans
