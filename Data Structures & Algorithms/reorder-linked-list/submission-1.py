# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node  
         
        positive = head
        negative = prev
        final = head

        #2->4->None
        #8->6->None
        # final 2->8 8->4       4->6 6-> None
        # positive None
        # negative None
        
        next_negative = negative

        while positive is not None and negative is not None:
            next_positive = positive.next
            final.next = negative
            final = final.next
            positive = next_positive

            next_negative = negative.next
            final.next = positive
            final = final.next
            negative = next_negative





