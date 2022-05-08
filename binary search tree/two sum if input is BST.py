# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.nums.append(node.val)
        self.inorder(node.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.nums = []
        self.inorder(root)

        i, j = 0, len(self.nums) - 1
        while i < j:
            sums = self.nums[i] + self.nums[j]
            if sums == k:
                return True
            elif sums < k:
                i = i + 1
            else:
                j = j - 1
        return False
