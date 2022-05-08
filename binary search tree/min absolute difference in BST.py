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
        self.dfs(node.left)
        self.nums.append(node.val)
        self.dfs(node.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.nums = []
        self.dfs(root)
        ans = float("inf")
        for i in range(1, len(self.nums)):
            ans = min(ans, self.nums[i] - self.nums[i - 1])
        return ans
