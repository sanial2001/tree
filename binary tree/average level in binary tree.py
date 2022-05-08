# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [(root.val, root)]
        ans = []
        while q:
            sums = 0
            for i in range(len(q)):
                val, node = q.pop(0)
                sums += val
                print(i, sums)
                if node.left:
                    q.append((node.left.val, node.left))
                if node.right:
                    q.append((node.right.val, node.right))
            # print(sums, i)
            ans.append(sums / (i + 1))
        return ans
