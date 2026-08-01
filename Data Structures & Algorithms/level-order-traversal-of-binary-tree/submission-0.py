# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # add to queue on what we need to travel
        # what i needed to realize here is that 
        # everytime we add something to the queue,
        queue = deque()
        queue.append(root)
        output = []

    
        while(queue):
            curr_len  = len(queue)
            level = []

            for i in range(curr_len):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if level:
                output.append(level)
        return output