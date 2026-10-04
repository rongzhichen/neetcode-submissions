class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        a1 = list1
        a2 = list2

        dummy = ListNode()
        cur = dummy

        while a1 is not None and a2 is not None:
            if a1.val <= a2.val:
                cur.next = a1
                a1 = a1.next
            else:
                cur.next = a2
                a2 = a2.next

            cur = cur.next

        # 至少一个链表已经用完，接上另一边
        if a1 is not None:
            cur.next = a1
        else:
            cur.next = a2

        return dummy.next