# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = float('-inf')

        def solve(node):
            if not node:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            self.answer = max(self.answer, left + right + node.val)
            return max(node.val, node.val + left, node.val + right)

        solve(root)
        return self.answer


