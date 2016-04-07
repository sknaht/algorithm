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

        def point(left, right):
            if not left or not right:
                return
            left.next = right
            point(left.left, left.right)
            point(left.right, right.left)
            point(right.left, right.right)

        if root:
            point(root.left, root.right)