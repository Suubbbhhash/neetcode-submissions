# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        a1=[]
        while cur1:
            a1.append(cur1.val)
            cur1=cur1.next
        x="".join(map(str,a1))
        cur2=l2
        a2=[]
        while cur2:
            a2.append(cur2.val)
            cur2=cur2.next
        y="".join(map(str,a2))
        rr=str(int(x[::-1])+int(y[::-1]))
        r=rr[::-1]
        res=ListNode(int(r[0]))
        curr=res
        for n in r[1:]:
            curr.next=ListNode(int(n))
            curr=curr.next
        return res


