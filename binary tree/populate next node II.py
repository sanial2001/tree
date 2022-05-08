"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = [root]
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # print(level)
            while level:
                node = level.pop(0)
                node.next = level[0] if level else None
        return root
