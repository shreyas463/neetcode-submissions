# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr, length = head, 0

        while curr != None:
            arr.append(curr)
            curr, length = curr.next, length + 1

        l, r = 0, length - 1
        last = head

        while l < r:
            arr[l].next = arr[r]  # Link the l-th node to the r-th node
            l += 1

            if l == r:
                last = arr[r]  # Reached the middle element
                break
            
            arr[r].next = arr[l]  # Link the r-th node to the next l-th node
            r -= 1

            last = arr[l]  # Update last to the current l-th node

        if last:
            last.next = None  # Terminate the list
