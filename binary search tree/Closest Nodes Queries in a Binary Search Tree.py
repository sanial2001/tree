# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import Optional, List


class Solution:
    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def reach(self, node, prev, target, path):
        if not node:
            if path == 'l':
                self.res.append([self.d[prev.val][0], prev.val])
            elif path == 'r':
                self.res.append([prev.val, self.d[prev.val][1]])
            return
        if target < node.val:
            self.reach(node.left, node, target, 'l')
        else:
            self.reach(node.right, node, target, 'r')

    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nums = self.inorder(root)
        n = len(nums)
        self.d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if i == 0:
                self.d[num].append(-1)
                self.d[num].append(nums[i + 1])
            elif i == n - 1:
                self.d[num].append(nums[i - 1])
                self.d[num].append(-1)
            else:
                self.d[num].append(nums[i - 1])
                self.d[num].append(nums[i + 1])
        # print(d.items())

        self.res = []
        for q in queries:
            if q in self.d:
                self.res.append([q, q])
            else:
                self.reach(root, None, q, '')

        return self.res
