# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ans, stack, node = [], [], root
        while node:
            stack.append(node)
            ans.append(node.val)
            node = node.left

        while stack:
            node = stack.pop().right
            if node:
                stack.append(node)
                ans.append(node.val)
                while node.left:
                    node = node.left
                    stack.append(node)
                    ans.append(node.val)
        return ans
