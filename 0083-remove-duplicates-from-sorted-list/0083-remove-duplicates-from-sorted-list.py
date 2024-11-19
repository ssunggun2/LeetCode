# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        node = head.next
        while node:
            if node.val == prev.val:
                temp = node.next
                prev.next = temp
                node = temp
            else:
                prev = node
                node = node.next
                
        return head
