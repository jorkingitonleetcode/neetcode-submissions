# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # a good node properties
        # if its parent is a good node then 
        # we can add  that to a valid list of ceilins
        # or valid list of floors.
        # we can traverse using bfs

        q =  deque([(root, float("-inf"))])
        good_nodes = 0
        while(q):
            curr, max_val = q.popleft()
            
            if curr.val >= max_val:
                good_nodes += 1
                max_val = curr.val
            # each node going has to be greater than its parent 

            if curr.left:
                q.append((curr.left, max_val))
                # minimum is the parent if it's right 
            if curr.right:
                q.append((curr.right, max_val))
        
        return good_nodes

            

            
            