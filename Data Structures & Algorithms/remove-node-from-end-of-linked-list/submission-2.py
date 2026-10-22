# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        prev = None
        curr = head
        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        
        delete_node = prev
        if n>=2:
            for i in range(n-1):
                delete_node = delete_node.next
        
        prev_1 = None
        curr = prev
        if n ==1:
            curr = prev.next
        while curr is not None:
            if curr.next == delete_node:
                nextnode = curr.next.next
            else:
                nextnode = curr.next

            curr.next = prev_1
            prev_1 = curr
            curr = nextnode
        return prev_1


            

        