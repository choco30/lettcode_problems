# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
    
        if slow is not None and slow.next is not None :
            fast=slow.next.next
        else:
            return False
        while(slow is not None and fast is not None and slow.next is not None and fast.next is not None):
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return False
