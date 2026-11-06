# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# # Access first node
# head

# # Access current node value
# curr.val

# # Access next node
# curr.next

# # Access next node's value
# curr.next.val

# # Move to next node
# curr = curr.next

# # Check if node exists
# if curr:

# # Traverse entire linked list
# while curr:

# # Change connection
# curr.next = prev

# # Check if linked list is empty
# if not head:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        
        return prev

        