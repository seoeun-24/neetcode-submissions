# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1=l1
        res1=[]
        while list1:
            res1.append(list1)
            list1=list1.next
        list2=l2
        res2=[]
        while list2:
            res2.append(list2)
            list2=list2.next

        carry=0
        res=[]
        for i in range(max(len(res1),len(res2))):
            val1= res1[i].val if i<len(res1) else 0
            val2= res2[i].val if i<len(res2) else 0

            add= val1+val2+carry
            digit=add%10
            carry=add//10
            res.append(digit)

        if carry:
            res.append(carry)
        head=ListNode(res[0])
        curr=head

        for nums in res[1:]:
            new_node=ListNode(nums)
            curr.next=new_node
            curr=curr.next
        return head



        