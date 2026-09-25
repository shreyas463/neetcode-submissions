# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(None) #at start we set curr to point to None
        curr=head

        while list1 or list2:
            if list1 is None:
                curr.next=list2
                return head.next
            if list2 is None:
                curr.next=list1
                return head.next
            if list1.val<list2.val: #if list 2 has bigger value than list1
                curr.next=list1 # Attach list1's node if it’s smaller (becomes curr)
                list1=list1.next # Move list1 to its next node
            else: #if list1 has has bigger value than list2
                curr.next=list2
                list2=list2.next
            curr=curr.next #keep moving the curr to next node
        return head.next


        