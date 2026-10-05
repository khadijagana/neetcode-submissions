# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            prev=None
            post=head.next
            curr=head
        else:
            return head


        while curr:
            curr.next=prev
            prev=curr
            curr=post
            if post:
                post=curr.next

        return prev


        