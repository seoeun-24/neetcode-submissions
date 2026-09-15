# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #ith node from the end of the list
        node=[]

        curr=head
        while curr:
            node.append(curr)
            curr= curr.next
        i=0
        while i<len(node):
                
            if len(node)==1:
                return None
            elif i==len(node)-n:
                if i==0:
                    head=head.next
                elif i==len(node)-1:
                    node[i-1].next = None
                else:
                    node[i-1].next= node[i+1]
            i+=1
        

        return head
            
            

