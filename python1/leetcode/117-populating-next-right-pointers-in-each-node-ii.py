# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        curr, next = root, TreeLinkNode(0)
        while curr:
            node, t = curr, next
            while node:
                if node.left:
                    t.next = node.left
                    t = t.next
                if node.right:
                    t.next = node.right
                    t = t.next
                node = node.next
            curr = next.next
            next = TreeLinkNode(0)




