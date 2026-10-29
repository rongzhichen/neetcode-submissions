# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, index, node))

        dummy = ListNode()
        cur = dummy

        while heap:
            value, index, node = heapq.heappop(heap)
            cur.next = node
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, index, node.next))
            node = node.next
            cur = cur.next
        return(dummy.next)



        

        return(dummy.next)

        
        

        

        

        