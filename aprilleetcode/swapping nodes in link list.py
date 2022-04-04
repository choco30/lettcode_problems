# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        point=head
        itr=head
        count=1
        count2=1
        size=1
        while(point.next!=None):
            size+=1
            point=point.next
        while(count!=k):
            count+=1
            itr=itr.next
        itr2=head  
        while(count2<=size-k):
            count2+=1
            itr2=itr2.next
        temp=itr.val
        itr.val=itr2.val
        itr2.val=temp
        return head
            
