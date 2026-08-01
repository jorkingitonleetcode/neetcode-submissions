# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        stack = []
        # use a stack
        curr = head
        while(curr != None):
            stack.append(curr)
            curr = curr.next
        

        new_head = stack.pop()
        curr = new_head
        while(len(stack) > 0):
            node = stack.pop()
            curr.next = node
            curr = curr.next
        curr.next = None
        
        return new_head