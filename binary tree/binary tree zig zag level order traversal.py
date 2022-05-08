# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [(root.val, root)]
        ans, flag = [], 0
        while q:
            temp = []
            for i in range(len(q)):
                val, node = q.pop(0)
                temp.append(val)
                if node.left:
                    q.append((node.left.val, node.left))
                if node.right:
                    q.append((node.right.val, node.right))
            if flag == 0:
                flag = 1
            else:
                temp = temp[::-1]
                flag = 0
            ans.append(temp)
        return ans
