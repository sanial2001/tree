# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root
        q = [root]
        k = 1
        while q:
            num = len(q)
            for i in range(num):
                node = q.pop(0)
                if k == depth:
                    return root
                if k == depth - 1:
                    new_node_left = TreeNode(val)
                    new_node_right = TreeNode(val)
                    new_node_left.left, new_node_right.right = node.left, node.right
                    node.left, node.right = new_node_left, new_node_right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            k += 1
        return root
