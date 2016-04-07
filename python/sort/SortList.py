# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeList(self, l1,l2):
        head = ListNode(0)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, curr, l1 = l1, l1, l1.next
            else:
                curr.next, curr, l2 = l2, l2, l2.next
        curr.next = l1 or l2
        return head.next

    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if not head or not head.next:
            return head

        # split the linked list into two part
        prev, fast, slow = None, head, head
        while fast and fast.next:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None

        # merge the two sorted linked list
        return self.mergeList(self.sortList(head), self.sortList(slow))
