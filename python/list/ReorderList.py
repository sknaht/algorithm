# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next: return head
        fast, slow, prev = head, head, None
        while fast and fast.next:
             slow, fast, prev = slow.next, fast.next.next, slow
        current, prev.next, prev = slow, None, None
        while current != None:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        l1, l2 = head, prev
        current = l1
        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.next
            current.next, current, l2 = l2, l2, l2.next
        return head
