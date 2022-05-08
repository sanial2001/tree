# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums, i, j):
        if i > j:
            return None
        mid = (i + j) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(nums, i, mid - 1)
        root.right = self.dfs(nums, mid + 1, j)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums) - 1)
