# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        l, r = self.dfs(node.left), self.dfs(node.right)
        self.sums.append(l + r + node.val)
        return l + r + node.val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.sums = []
        total = self.dfs(root)
        ans = 0
        for val in self.sums:
            ans = max(ans, val * (total - val))
        return ans % (10 ** 9 + 7)
