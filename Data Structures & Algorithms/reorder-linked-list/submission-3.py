# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr=[]
        curr,length=head,0
        while curr!=None:
            arr.append(curr)
            curr,length=curr.next,length+1

        l,r=0,length-1
        last=head
        while l<r:
            arr[l].next=arr[r]
            l+=1

            if l==r:
                last=arr[r]
                break
            
            arr[r].next=arr[l]
            r-=1
            last=arr[l]
        if last:
            last.next=None
        

        