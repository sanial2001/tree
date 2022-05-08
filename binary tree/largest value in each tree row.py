# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            max_row = float("-inf")
            for i in range(len(q)):
                node = q.pop(0)
                if node.val > max_row:
                    max_row = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_row)
        return ans
