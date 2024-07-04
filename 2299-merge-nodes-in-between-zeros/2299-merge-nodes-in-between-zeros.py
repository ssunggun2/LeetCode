# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        node = head.next
        s = 0
        while node:
            if node.val != 0:
                s += node.val
            else:
                current.next = ListNode(s)
                current = current.next
                s = 0
            node = node.next
        return dummy.next