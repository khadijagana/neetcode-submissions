# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        pre=None
        next=None
        while current:
            next=current.next
            current.next=pre
            pre=current
            current=next

        
        return pre


    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None: return
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next        

        second=slow.next
        slow.next=None

        first=head
        second=self.reverseList(second)
        while first and second:
            next_first=first.next
            next_second=second.next
            first.next=second
            second.next=next_first
            first=next_first
            second=next_second

        


