# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        ans = None
        while q:
            k = 0
            for i in range(len(q)):
                node = q.pop(0)
                if k == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                k += 1
        return ans
