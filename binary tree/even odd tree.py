# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        k = 0

        while q:
            temp = [float("-inf")] if k % 2 == 0 else [float("inf")]
            for i in range(len(q)):
                node = q.pop(0)
                if k % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if node.val <= temp[-1]:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False
                    if node.val >= temp[-1]:
                        return False
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            k += 1

        return True
