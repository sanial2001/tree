# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        max_sum = float("-inf")
        level, ans = 1, 1
        while q:
            sums = 0
            for i in range(len(q)):
                node = q.pop(0)
                sums += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if sums > max_sum:
                max_sum = sums
                ans = level
            level += 1
        return ans
