# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = [root]
        res = 0

        while q:
            num = len(q)
            temp = []
            for i in range(num):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            d = {val: i for i, val in enumerate(sorted(temp))}
            seen = set()
            for i in range(len(temp)):
                cnt = 0
                while i not in seen and i != d[temp[i]]:
                    seen.add(i)
                    cnt += 1
                    i = d[temp[i]]
                res += max(0, cnt - 1)

        return res
