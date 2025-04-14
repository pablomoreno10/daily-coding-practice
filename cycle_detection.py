# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #At least one node in the list can be visited again using next else false
        #if last head.next == null then false
        visited = set()
        current = head
        while current:
            if current in visited: #can be visited again return True
                return True
            visited.add(current)
            current = current.next
        return False
