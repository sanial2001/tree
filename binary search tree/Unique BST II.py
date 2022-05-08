# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, low, high):
        if low == high:
            return [TreeNode(low)]
        if low > high:
            return [None]
        res = []
        for i in range(low, high + 1):
            left = self.construct(low, i - 1)
            right = self.construct(i + 1, high)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.construct(1, n)
