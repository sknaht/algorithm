class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(-1)
        dummy.next, curr = head, head
        while curr and curr.next:
            next = curr.next
            if next.val < curr.val:
                tmp = dummy
                while tmp.next and tmp.next.val < next.val:
                    tmp = tmp.next
                curr.next = next.next
                next.next = tmp.next
                tmp.next = next
            else:
                curr = curr.next


        return dummy.next

t = ListNode(5)
t.next = ListNode(2)
t.next.next = ListNode(1)
t.next.next.next     = ListNode(4)

print Solution().insertionSortList(t)