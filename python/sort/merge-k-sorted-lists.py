# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):

        return self.merge(0, len(lists) - 1, lists)

    def merge(self, start, end, lists):
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = (start + end) / 2
        left = self.merge(start, mid, lists)
        right = self.merge(mid + 1, end, lists)
        tmp = ListNode(-1)
        curr = tmp
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return tmp.next

x = ListNode(0)
x.next = ListNode(5)

a = [
    ListNode(1),
    ListNode(4),
    ListNode(3),
    x
]

print Solution().mergeKLists(a)




