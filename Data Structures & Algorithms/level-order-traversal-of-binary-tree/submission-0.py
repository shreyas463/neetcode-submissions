# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result=[]

        q=deque([root])

        while q:
            max_nodes=len(q) #storing the number of nodes in queue
            curr_level=[] #storing the no of nodes at currentlvel

            for _ in range(max_nodes):
                node=q.popleft() #pop nodes
                curr_level.append(node.val) #add value of node to the 

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            result.append(curr_level)
            #Once you’ve collected all nodes of the current level, add the level list to result
        return result








        