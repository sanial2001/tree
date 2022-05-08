# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left, right = self.dfs(node.left), self.dfs(node.right)
        val = left + right + node.val
        self.d[val] = self.d.get(val, 0) + 1
        return val

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.d = {}
        self.dfs(root)
        ans = []
        # print(self.d.items())
        max_cnt = max(self.d.values())
        for key in self.d:
            if self.d[key] == max_cnt:
                ans.append(key)
        return ans
