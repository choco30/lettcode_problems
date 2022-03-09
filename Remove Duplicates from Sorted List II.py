leetcode problem 82
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent=ListNode(0,head)
        slow=sent
        fast=head
        while fast is not None:
            if fast.next is not None and fast.val==fast.next.val:
                while fast.next and fast.val==fast.next.val:
                    fast=fast.next
                slow.next=fast.next
            else:
                slow=slow.next
            fast=fast.next    
        return sent.next
