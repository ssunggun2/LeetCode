# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        flags = []
        last_val = head.val
        node = head
        while node:
            if node.val > last_val:
                flags.append(1)
            elif node.val == last_val:
                flags.append(0)
            else:
                flags.append(-1)
            last_val = node.val
            if not node.next:
                break
            node = node.next
        flags.append(0)
        locations = []
        for i in range(len(flags) - 1):
            if flags[i] * flags[i + 1] == -1:
                locations.append(i + 1)
        if len(locations) < 2:
            return [-1, -1]
        max_distance = locations[-1] - locations[0]
        min_distance = min([ locations[i+1] - locations[i] for i in range(len(locations) - 1)])
        return [min_distance, max_distance]