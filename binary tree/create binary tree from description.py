# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        kids, parent = set(), set()
        d = collections.defaultdict(list)
        for par, kid, left in descriptions:
            parent.add(par)
            kids.add(kid)
            d[par].append([kid, left])

        parent.difference_update(kids)
        root = TreeNode(parent.pop())

        q = [(root)]
        while q:
            node = q.pop(0)
            for kid, left in d[node.val]:
                new_node = TreeNode(kid)
                q.append(new_node)
                if left:
                    node.left = new_node
                else:
                    node.right = new_node

        return root
