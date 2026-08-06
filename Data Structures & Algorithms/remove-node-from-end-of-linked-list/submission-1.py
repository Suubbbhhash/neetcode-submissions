class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = []
        curr = head

        while curr:
            res.append(curr.val)
            curr = curr.next

        del res[-n]

        if not res:      # List became empty
            return None

        head = ListNode(res[0])
        curr = head

        for p in res[1:]:
            curr.next = ListNode(p)
            curr = curr.next

        return head