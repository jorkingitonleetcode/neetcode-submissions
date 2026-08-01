# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # im naive for this solution, i need to check the min and max 
        # for this current tree 
        # going down means i need to get the absolute ceiling and floor, usually 
        # Here is a good test case: 
        # this is an issue: 
        #      5
        #     / \
        #    4   6
        #       /  \
        #      3    7
        q = deque([(root,float("-inf"), float("inf") )])

        while(q):
            curr, min_val, max_val = q.popleft()
            if not (min_val < curr.val < max_val):
                return False 

            if curr.left:
                q.append((curr.left, min_val, curr.val))
            if curr.right:
                q.append((curr.right, curr.val, max_val))
                

        
        return True 