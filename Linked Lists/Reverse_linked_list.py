# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        #point curr to head and prev to none (space next to head)
        
        while curr is not None: #same as while curr
            temp = curr.next #temp new value is current next
            curr.next = prev #current next new value is prev
            prev = curr #prev new value is current
            curr = temp #current new value is temp
        return prev 
