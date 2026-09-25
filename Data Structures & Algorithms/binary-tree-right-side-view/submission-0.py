# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        q=deque([root])

        while q:
            allele=len(q) #holds the number of nodes at that level.

            for i in range(allele):
                node=q.popleft()
 
                if i==allele-1: #adding the last node to result(rightside)
                    result.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return result
