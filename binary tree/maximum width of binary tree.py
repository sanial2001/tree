# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(0, root)]
        ans = 0
        while q:
            temp = []
            for i in range(len(q)):
                ind, node = q.pop(0)
                temp.append(ind)
                if node.left:
                    q.append((2 * ind + 1, node.left))
                if node.right:
                    q.append((2 * ind + 2, node.right))
            ans = max(ans, max(temp) - min(temp) + 1)
        return ans
