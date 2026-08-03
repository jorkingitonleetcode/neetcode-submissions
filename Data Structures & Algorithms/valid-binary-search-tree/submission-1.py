# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        while(q):
            curr_len = len(q)
            curr = q.popleft()

            if curr.right and curr.val >= curr.right.val :
                return False
            elif curr.left and curr.val <= curr.left.val:
                return False
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
                

        
        return True 