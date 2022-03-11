#leetcode problem 61
# problem is to rotatae the link list right k no of time

# Approach- To count  the no of elements in list(suppose 'n')
#so after n nuber of rotation we will get the same link list
# so divide k with total no of nodes and store the remainder, that will be the number of rotation you need to do



```class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        itr=head
        start=itr
        count=0
        while start is not None:
            count+=1
            start=start.next
            
        if head is None:
            return None  
        if head.next is None:
            return head            
        k=k%count
        print(count)
        print(k)
        prev=itr
        if head is None:
            return None  
        if head.next is None:
            return head
        
        for i in range(k):
            while itr.next is not None:
                prev=itr
                itr=itr.next
            prev.next=None
            itr.next=head
            head=itr
        return head```
