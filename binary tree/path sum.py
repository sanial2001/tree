# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, sums, k):
        if not node:
            return
        sums += node.val
        if not node.left and not node.right:
            if sums == k:
                self.ans = True
            return
        self.dfs(node.left, sums, k)
        self.dfs(node.right, sums, k)
        sums -= node.val

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False
        self.dfs(root, 0, targetSum)
        return self.ans
