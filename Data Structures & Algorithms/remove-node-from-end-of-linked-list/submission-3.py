# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=[]
        curr=head
        while curr:
            res.append(curr)
            curr=curr.next

        IndexNode=len(res)-n

        if len(res)-n==0:
            return head.next

        res[IndexNode-1].next=res[IndexNode].next
        return head
