# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):

        node = root

        def right_most_height(node):
            t = node
            c = 0
            while t:
                c += 1
                t = t.right
            return c

        h = 0
        while node:
            h += 1
            node = node.left


        node = root
        level = 1
        count = 0
        while node:
            left, right = node.left, node.right

            t = right_most_height(left)

            # left tree is complete, with height = t (height - level)
            if t + level == h:
                count += 2 ** t
                node = right

            # right tree is complete, with height = t (height - level - 1)
            else:
                count += 2 ** t
                node = left

            level += 1

        return count







