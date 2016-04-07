# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(a, b):
            if not a or not b:
                return a or b
            head = ListNode(0)
            curr = head
            while a and b:
                if a.val < b.val:
                    curr.next = a
                    a = a.next
                else:
                    curr.next = b
                    b = b.next
                curr = curr.next
            if a or b:
                curr.next = a or b
            return head.next
        
        def sort(node):
            if not node or not node.next:
                return node
            head = ListNode(0)
            fast, slow, head.next = head, head, node

            while fast and fast.next:
                fast, slow = fast.next.next, slow.next
            fast = slow.next
            slow.next = None
            return merge(sort(node), sort(fast))
        return sort(head)
            

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
b = Solution().sortList(a)
print b
        