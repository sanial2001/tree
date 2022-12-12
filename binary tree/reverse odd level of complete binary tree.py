# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        level = 0

        while q:
            num = len(q)
            temp = []
            for i in range(num):
                node = q.pop(0)
                temp.append((node, node.val))
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 != 0:
                # print(len(par), len(temp))
                temp_copy = temp.copy()
                for p in par:
                    p.left.val = temp_copy.pop()[1]
                    p.right.val = temp_copy.pop()[1]
            par = []
            for i, j in temp:
                # print(j)
                par.append(i)
            # print("\n")
            level += 1

        return root
