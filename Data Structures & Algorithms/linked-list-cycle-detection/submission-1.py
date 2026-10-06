# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hash_list={}
        current=head
        while current:
            if current.next==None: 
                return False
            if current in hash_list:
                return True
            else:
                hash_list[current]=current.next
                current=current.next
        return False