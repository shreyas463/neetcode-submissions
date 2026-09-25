# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val>root.val and q.val> root.val: #if both bigg than root, we look right
                root=root.right
            elif p.val<root.val and q.val<root.val: #if both sm than root, we look left
                root=root.left
            else:
                return root #if one bigg or one small (split), then root is LCA
        