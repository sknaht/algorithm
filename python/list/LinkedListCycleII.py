# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        h1 = head
        h2 = head
        while h2 and h2.next:
            h1, h2 = h1.next, h2.next.next
            if h1 is h2:
                h2 = head
                while h1 is not h2:
                    h1, h2 = h1.next, h2.next
                return h1
        return None

