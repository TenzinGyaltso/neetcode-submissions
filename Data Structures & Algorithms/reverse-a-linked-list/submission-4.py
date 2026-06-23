# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        now = head
        while now:
            next_node = now.next
            now.next = prev
            prev = now
            now = next_node
            
        return prev

            
