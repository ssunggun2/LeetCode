# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy
        
        # Traverse the list
        while current.next:
            if current.next.val == val:
                # Skip the node with the target value
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next