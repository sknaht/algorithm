# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        h = depth(root)
        node = root
        total = 0
        for i in xrange(h):
            hr = depth(node.right)
            if hr == h - i - 1:
                node = node.right
            else:
                node = node.left
            total += 2 ** hr

        return total


