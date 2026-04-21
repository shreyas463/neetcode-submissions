# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node to act as the head of the merged list
        tail = dummy  # This will be the last node in the merged list

        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Append the smaller node to the merged list
                list1 = list1.next  # Move to the next node in list1
            else:
                tail.next = list2  # Append the smaller node to the merged list
                list2 = list2.next  # Move to the next node in list2
            tail = tail.next  # Move the tail pointer to the last node in the merged list

        # Append the remaining nodes from the non-exhausted list
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # Return the head of the merged list
