#linked list 
#tow pointers
#shift the fast pointer by two (going twice as fast as the slow pointer)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        start = head
        end = head
        while end and end.next:
                start = start.next
                end = end.next.next
        return start
            
        