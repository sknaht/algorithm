# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = ListNode(0)
        tmp = ListNode(0)

        result.next = head
        head = result

        while head.next:
            tail = head.next
            for i in xrange(k):
                if tail:
                    tail = tail.next
                else:
                    return result.next

            next_head = head.next
            while head.next != tail:
                t = head.next
                head.next = t.next
                t.next = tmp.next
                tmp.next = t

            next_head.next = head.next
            head.next = tmp.next
            tmp.next = None

            head = next_head

        return result.next


a = ListNode(1)
a.next = ListNode(2)
Solution().reverseKGroup(a, 1)
