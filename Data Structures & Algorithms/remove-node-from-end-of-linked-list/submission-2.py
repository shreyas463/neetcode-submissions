# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        
        # Advance fast to the nth position
        for _ in range(n):
            fast = fast.next
            
        # If fast is None, it means the list has exactly n nodes
        # and the head needs to be removed
        if not fast:
            return head.next
        
        # Move both fast and slow pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        # Return the head of the modified list
        return head
