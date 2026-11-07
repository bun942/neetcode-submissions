# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        dummy = ListNode(0)
        curr = dummy 

        while p1 and p2 :
            if p1.val < p2.val:
                curr.next = ListNode(p1.val)
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                p2 = p2.next
            curr = curr.next
        
        while p1:
            curr.next = ListNode(p1.val)
            p1 = p1.next
            curr = curr.next
        
        while p2:
            curr.next = ListNode(p2.val)
            p2 = p2.next
            curr = curr.next
        
        return dummy.next
