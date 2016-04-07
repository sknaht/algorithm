"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):

        num, t = 0, head
        while t:
            num += 1
            t = t.next
        self.head = head
        return self.convert(0, num)

    def convert(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        left = self.convert(start, mid)
        current = TreeNode(self.head.val)
        self.head = self.head.next
        current.left = left
        current.right = self.convert(mid + 1, end)
        return current

if __name__ == "__main__":
    head = ListNode(1)
    result = Solution().sortedListToBST(head)
    print result.val
    print result.left.val
    print result.right.val
