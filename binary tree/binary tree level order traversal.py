# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [(root.val, root)]
        ans = []
        while q:
            temp = []
            for i in range(len(q)):
                val, node = q.pop(0)
                temp.append(val)
                if node.left:
                    q.append((node.left.val, node.left))
                if node.right:
                    q.append((node.right.val, node.right))
            ans.append(temp)
        return ans
