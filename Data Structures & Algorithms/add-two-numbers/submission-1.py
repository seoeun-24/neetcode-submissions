# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1= l1
        res1=[]
        while curr1:
            res1.append(curr1)
            curr1=curr1.next
        curr2= l2
        res2=[]
        while curr2:
            res2.append(curr2)
            curr2=curr2.next

        carry = 0

        dummy = ListNode(0)
        curr = dummy

        for i in range(max(len(res1), len(res2))):

            val1 = res1[i].val if i < len(res1) else 0
            val2 = res2[i].val if i < len(res2) else 0

            add = val1 + val2 + carry

            digit = add % 10
            carry = add // 10

            new_node = ListNode(digit)
            curr.next = new_node
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next







        
        

        