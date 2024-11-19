# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        node = head
        temp = head
        count = 0
        while node:
            count += 1
            node = node.next
        for i in range(count // 2):
            temp = temp.next
        return temp
