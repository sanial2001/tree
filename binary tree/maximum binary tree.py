# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        index = nums.index(max(nums[start:end + 1]))
        root = TreeNode(nums[index])
        root.left = self.solve(nums, start, index - 1)
        root.right = self.solve(nums, index + 1, end)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.solve(nums, 0, len(nums) - 1)
